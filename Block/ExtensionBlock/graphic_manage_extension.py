import Block.ExtensionBlock.extension_block as extension_block


class GraphicManageExtension(extension_block.ExtensionBlock):
    extension_code = 0xf9

    def __init__(self, data: bytes, pos: int):
        super().__init__(0xf9)
        pos += 1

        self.size = data[pos]
        pos += 1

        self.reserved = data[pos] >> 5
        self.disposal_method = (data[pos] >> 2) & 0b111
        self.user_input_flag = bool((data[pos] >> 1) & 0b1 == 1)
        self.transparent_color_flag = bool(data[pos] & 0b1 == 1)
        pos += 1

        # Seconds
        self.delay_time = (data[pos] + (data[pos+1] << 8)) / 100
        pos += 2

        self.transparent_color_index = data[pos]
        pos += 1

    def __str__(self):
        return "Graphic ext: \n" \
               "Extension: {0.extension_code}\n" \
               "Size: {0.size}\n" \
               "Reserved: {0.reserved}\n" \
               "Disposal method: {0.disposal_method}\n" \
               "User input flag: {0.user_input_flag}\n" \
               "Transparent color flag: {0.transparent_color_flag}\n" \
               "Delay time: {0.delay_time}\n" \
               "Transparent color index: {0.transparent_color_index}\n" \
               .format(self)

    def __len__(self):
        return 6 + 1
