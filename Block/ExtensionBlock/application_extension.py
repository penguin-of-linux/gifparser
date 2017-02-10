import Block.ExtensionBlock.extension_block as extension


class ApplicationExtension(extension.ExtensionBlock):
    extension_code = 0xff

    def __init__(self, data: bytes, pos: int):
        super().__init__(0xff)
        pos += 1

        self.block_size = data[pos]
        pos += 1

        self.identifier = data[pos:pos+8]
        pos += 8

        self.authentication_code = data[pos:pos+3]
        pos += 3

        block_size = data[pos]
        pos += 1
        self.__data_size = block_size
        self.application_data = data[pos:block_size + pos]
        pos += block_size

    def __str__(self):
        return "Application ext:\n" \
               "Block code: {0.block_code}\n" \
               "Extension code: {0.extension_code}\n" \
               "Block size: {0.block_size}\n" \
               "Identifier: {0.identifier}\n" \
               "Authentication: {0.authentication_code}\n" \
               "Application data: {0.application_data}\n" \
               .format(self)

    def __len__(self):
        return 13 + self.__data_size + 1
