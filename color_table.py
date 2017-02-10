class ColorTable:
    def __init__(self, data: bytes, pos: int, size: int):
        self.colors = list()
        i = pos
        while i < pos + (2 ** (size + 1)) * 3:
            color = data[i:i+3]
            self.colors.append(color)
            i += 3

    def __str__(self):
        result = "Color table:\n"
        for color in self.colors:
            result += "{0[0]} {0[1]} {0[2]}\n".format(color)
        return result

    def __len__(self):
        return len(self.colors) * 3
