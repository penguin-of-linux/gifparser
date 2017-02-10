import Block.block as block


class ImageDescriptor(block.Block):
    block_code = 0x2c

    def __init__(self, data: bytes, pos: int):
        super().__init__(0x2c)

        self.image_left_position = data[pos] + (data[pos+1] << 8)
        pos += 2

        self.image_top_position = data[pos] + (data[pos+1] << 8)
        pos += 2

        self.width = data[pos] + (data[pos+1] << 8)
        pos += 2

        self.height = data[pos] + (data[pos+1] << 8)
        pos += 2

        self.local_color_table_flag = bool((data[pos] >> 7) & 1 == 1)
        self.interface_flag = bool((data[pos] >> 6) & 1 == 1)
        self.sort_flag = bool((data[pos] >> 5) & 1 == 1)
        self.reserved = (data[pos] >> 3) & 0b111
        self.local_color_table_size = data[pos] & 0b111
        pos += 1

    def __str__(self):
        return "Image descriptor:\n" \
               "Block code: {0.block_code}\n" \
               "Image left position: {0.image_left_position}\n" \
               "Image top position: {0.image_top_position}\n" \
               "Width: {0.width}\n" \
               "Height: {0.height}\n" \
               "Local color table flag: {0.local_color_table_flag}\n" \
               "Interface: {0.interface_flag}\n" \
               "Sort flag: {0.sort_flag}\n" \
               "Reserved: {0.reserved}\n" \
               "Local color table size: {0.local_color_table_size}\n" \
               .format(self)

    def __len__(self):
        return 9 + 1
