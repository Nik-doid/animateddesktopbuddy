import sys
import psutil
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QMovie, QPainter, QImage
from PyQt5.QtCore import Qt, QTimer, QRect

class CatWidget(QWidget):
    def __init__(self, gif_path):
        super().__init__()

        # Frameless and transparent
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Load GIF
        self.movie = QMovie(gif_path)
        self.movie.frameChanged.connect(self.update)  # Trigger repaint on each frame
        self.movie.start()

        # Wait for the first frame to load before setting crop (safe for some GIFs)
        self.movie.jumpToFrame(0)
        full_size = self.movie.currentPixmap().size()
        width = full_size.width()
        height = full_size.height()

        # Crop 60% from top, and 15% from both left and right
        left_crop = int(width * 0.35)
        right_crop = int(width * 0.4)
        top_crop = int(height * 0.6)
        bot_crop = int(height * 0.1)

        new_width = width - left_crop - right_crop
        new_height = height - top_crop - bot_crop

        self.crop_rect = QRect(left_crop, top_crop, new_width, new_height)
        self.resize(self.crop_rect.size())

        # Dragging
        self.drag_position = None

        # CPU-based animation speed
        self.timer = QTimer()
        self.timer.timeout.connect(self.adjust_speed)
        self.timer.start(1000)

    def adjust_speed(self):
        cpu = psutil.cpu_percent()
        min_speed = 50    # slowest speed at 0% CPU
        max_speed = 300   # fastest speed at 100% CPU
        speed = min_speed + int((max_speed - min_speed) * (cpu / 100))
        self.movie.setSpeed(speed)

    def paintEvent(self, event):
        painter = QPainter(self)
        frame = self.movie.currentPixmap()
        if not frame.isNull():
            cropped = frame.copy(self.crop_rect)

        # Convert to QImage to manipulate pixels
            img = cropped.toImage().convertToFormat(QImage.Format_ARGB32)

            for y in range(img.height()):
                for x in range(img.width()):
                    color = img.pixelColor(x, y)
                    if color.red() < 10 and color.green() < 10 and color.blue() < 10:
                        color.setAlpha(0)  # Make black fully transparent
                        img.setPixelColor(x, y, color)

            painter.drawImage(0, 0, img)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.drag_position and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)

    def mouseReleaseEvent(self, event):
        self.drag_position = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cat = CatWidget("a.gif") #replace file with your gif try gif with transparent bg
    cat.show()
    sys.exit(app.exec_())
