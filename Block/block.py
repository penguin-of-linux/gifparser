class Block:
    terminal_byte = 0x00

    def __init__(self, block_code: int):
        self.block_code = block_code
