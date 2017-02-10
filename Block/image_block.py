class ImageBlock:
    def __init__(self, data: bytes, pos: int):
        self.min_lzw_code = data[pos]
        pos += 1

        self.blocks = []
        size = data[pos]
        while size:
            pos += 1
            self.blocks.append(data[pos:pos + size])
            pos += size
            size = data[pos]

    def __str__(self):
        result = "Image block:\n"
        result += "Min LZW code: {}\n".format(self.min_lzw_code)

        for block in self.blocks:
            result += "{} bytes\n".format(str(len(block)))

        return result

    def __len__(self):
        last_block = self.blocks[len(self.blocks) - 1]
        return 256 * (len(self.blocks) - 1) + len(last_block) - 1
