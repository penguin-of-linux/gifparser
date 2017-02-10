import sys
import argparse

from painter import GifPainter
from gif_parser import GifParser
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="GIF parser 1.0")
    parser.add_argument("-p", "--painter", action="store_true", help="Use flag for paint GIF image")
    parser.add_argument("-f", "--file", type=str, default="sample.gif", help="File for parsing")
    args = parser.parse_args()

    if args.painter:
        app = QApplication(sys.argv)
        painter = GifPainter(args.file)
        sys.exit(app.exec_())
    else:
        with open(args.file, "rb") as f:
            data = f.read()
        for block in GifParser.parse_all(data):
            print(block)
