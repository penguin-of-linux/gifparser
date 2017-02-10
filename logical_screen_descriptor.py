class LSD:
    def __init__(self, data: bytes):
        self.width = data[6] + (data[7] << 8)
        self.height = data[8] + (data[9] << 8)
        self.global_color_table_using = bool((data[10] >> 7) == 1)
        self.color_resolution = (data[10] >> 4) & 0b111
        self.sorting = bool((data[10] >> 3) & 1 == 1)
        self.global_color_table_size = data[10] & 0b111
        self.background_color_index = data[11]
        self.pixel_aspect_ratio = data[12]

    def __str__(self):
        return "LSD:\n" \
               "Width: {0.width}\n" \
               "Height: {0.height}\n" \
               "Global color table using: {0.global_color_table_using}\n" \
               "Color resolution: {0.color_resolution}\n" \
               "Sorting: {0.sorting}\n" \
               "Global color table size: {0.global_color_table_size}\n" \
               "Background color index: {0.background_color_index}\n" \
               "Pixel aspect ration: {0.pixel_aspect_ratio}\n".format(self)
