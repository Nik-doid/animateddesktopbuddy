# Animated Cat Widget 🐱

A frameless, draggable animated cat GIF widget with CPU-based animation speed — built with PyQt5, designed especially for Ubuntu users.  
Because who doesn’t love a cute cat on their desktop?

---

## Requirements

- Python 3.6 or higher
- PyQt5
- psutil
- pillow

---

## Installation

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install the required packages:

```bash
pip install -r requirements.txt

```

## How to use

-Simply run the script

```bash
python3 runcat_linux.py

```
Dont forget to add a gif file in root and replace the file name in runcat_linux.py.[GIF](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHVhbXVhbmtyYXU0ZDZ5ajRzdjkwb3ZiOW84ZzhhNDIwbjNxNWx6eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aiqIqtW2utnkk/giphy.gif)
Gif that i am using.(Make the background transparent)

## Notes

The animation speed adjusts based on your CPU usage (requires psutil).

If you don’t have psutil or pillow installed, some features may be limited but the widget will still run.

## Finally

Enjoy your new desktop buddy!

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
