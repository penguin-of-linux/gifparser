import gif_image
import lzw

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from time import sleep


class GifPainter(QWidget):
    def __init__(self, file):
        super().__init__()

        self.is_ready_to_draw = False
        self.image = None
        self.current_frame = 0
        self.colors = []
        self.set_image(file)

        self.next_frame_button = QPushButton("Next frame", self)
        self.next_frame_button.clicked.connect(self.next_frame)

        self.prev_frame_button = QPushButton("Previous frame", self)
        self.prev_frame_button.clicked.connect(self.prev_frame)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        # hbox.addWidget(self.set_image_button)
        hbox.addWidget(self.prev_frame_button)
        hbox.addWidget(self.next_frame_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle("GIF painter: " + file)
        if self.image is not None:
            self.setGeometry(100, 100,
                            self.image.logical_screen_descriptor.width,
                            self.image.logical_screen_descriptor.height + 200)
        self.show()

    def set_image(self, file):
        try:
            with open(file, "rb") as f:
                data = f.read()
        except FileNotFoundError:
            print("File not found")
            return

        self.image = gif_image.GifImage(data)

        for frame in self.image.frames:
            data = bytes([])
            for block in frame.image_block.blocks:
                data = data + block
            self.colors.append(lzw.LZW.decode(data, frame.image_block.min_lzw_code))
        self.is_ready_to_draw = True

    def next_frame(self):
        if self.image is None:
            print("File not loaded")
            return

        if self.current_frame < len(self.image.frames) - 1:
            self.current_frame += 1
        else:
            self.current_frame = 0
        self.is_ready_to_draw = True
        self.update()

    def prev_frame(self):
        if self.image is None:
            print("File not loaded")
            return

        if self.current_frame > 0:
            self.current_frame -= 1
        else:
            self.current_frame = len(self.image.frames) - 1
        self.is_ready_to_draw = True
        self.update()

    def paintEvent(self, QPaintEvent):
        if self.image is None or not self.is_ready_to_draw:
            return

        qp = QPainter()
        qp.begin(self)

        frame = self.image.frames[self.current_frame]
        colors = self.colors[self.current_frame]

        for cur_pixel, color in enumerate(colors):
            try:
                r = frame.color_table.colors[color][0]
                g = frame.color_table.colors[color][1]
                b = frame.color_table.colors[color][2]

                x = cur_pixel % frame.descriptor.width
                y = cur_pixel // frame.descriptor.height

                qp.setPen(QColor(r, g, b))
                qp.drawPoint(x, y)
            except Exception as e:
                # Честно - не успел исправить баг поломки палитры
                pass

        qp.end()
        self.is_ready_to_draw = False
