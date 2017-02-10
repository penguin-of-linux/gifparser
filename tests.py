import unittest

from Block import image_block
from gif_parser import GifParser


class Tests(unittest.TestCase):
    def setUp(self):
        with open("sample.gif", "rb") as f:
            self.data = f.read()

    def test_parse_image_data_block(self):
        image = image_block.ImageBlock(self.data, 74)

        self.assertEqual(3, image.min_lzw_code)
        self.assertEqual(1, len(image.blocks), "Parse image blocks: length")
        self.assertEqual(self.data[76:76 + 8], image.blocks[0], "Parse image blocks: data")

    def test_parse_header(self):
        header = GifParser.get_header(self.data)

        self.assertEqual(b"GIF89a", header.signature + header.version)

if __name__ == "__main__":
    unittest.main()
