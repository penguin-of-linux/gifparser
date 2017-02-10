import Block.ExtensionBlock.extension_block as ext


class PlainTextExtension(ext.ExtensionBlock):
    extension_code = 0x01

    def __init__(self, data: bytes, pos: int):
        super().__init__(0x01)
        pos += 1

        self.block_size = data[pos]
        pos += 1

        self.text_left_position = data[pos] + (data[pos+1] << 8)
        pos += 2

        self.image_top_position = data[pos] + (data[pos+1] << 8)
        pos += 2

        self.width = data[pos] + (data[pos+1] << 8)
        pos += 2

        self.height = data[pos] + (data[pos+1] << 8)
        pos += 2

        self.char_cell_width = data[pos]
        pos += 1

        self.char_cell_height = data[pos]
        pos += 1

        self.text_foreign_color_index = data[pos]
        pos += 1

        self.text_background_color_index = data[pos]
        pos += 1

        self.blocks = []
        size = data[pos]
        while size != 0x00:
            pos += 1
            self.blocks.append(data[pos:pos + size])
            pos += size
            size = data[pos]

    def __str__(self):
        result = "Plain text extension:\n" \
                 "Extension code: {0.extension_code}\n" \
                 "Block size: {0.block_size}\n" \
                 "Text left position: {0.text_left_position}\n" \
                 "Text top position: {0.text_top_position}\n" \
                 "Width: {0.width}\n" \
                 "Height: {0.height}\n" \
                 "Character cell width: {0.char_cell_width}\n" \
                 "Character cell height: {0.char_cell_height}\n" \
                 "Text foreign color index: {0.text_foreign_color_index}\n" \
                 "Text background color index: {0.text_background_color_index}\n" \
                 .format(self)

        for block in self.blocks:
            result += " {} bytes\n".format(len(block))

        return result

    def __len__(self):
        last_block = self.blocks[len(self.blocks) - 1]
        return 14 + (256 * (len(self.blocks) - 1) + len(last_block) - 1)
