import Block.block as block


class ExtensionBlock(block.Block):
    block_code = 0x21

    def __init__(self, extension_code: int):
        super().__init__(0x21)

        self.extension_code = extension_code
