import Block.ExtensionBlock.extension_block as ext
import Block.block as block


class CommentExtension(ext.ExtensionBlock):
    extension_code = 0xfe

    def __init__(self, data: bytes, pos: int):
        super().__init__(0xfe)
        pos += 1

        self.__text_size = 0
        self.text = -1
        while data[pos] != block.Block.terminal_byte:
            block_size = data[pos]
            pos += 1
            if self.text == -1:
                self.text = data[pos:pos+block_size]
            else:
                self.text += data[pos:pos+block_size]
            self.__text_size += block_size
            pos += block_size

    def __len__(self):
        return 1 + self.__text_size

    def __str__(self):
        return "Comment ext:\n" \
               "Extension code: {0.extension_code}\n" \
               "Text: {0.text}\n" \
               .format(self)
