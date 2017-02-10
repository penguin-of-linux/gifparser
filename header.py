class Header:
    def __init__(self, data: bytes):
        self.signature = data[:3]
        self.version = data[3:6]

    def __str__(self):
        return "Header:\n" \
               "Signature: {0.signature}\n" \
               "Version: {0.version}\n\n".format(self)
