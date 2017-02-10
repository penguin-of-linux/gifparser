class LZW:
    @staticmethod
    def decode(data: bytes, min_lzw_code_size: int):
        result = []
        data = LZW.__to_binary_string(data)
        pos = 0
        prev_indices = None
        indices = LZW.__init_dict(min_lzw_code_size)
        # size = min_lzw_code_size + 1

        while pos < len(data):
            size = len(indices).bit_length()
            code = int(data[pos:pos + size][::-1], 2)
            pos += size
            if code in indices:
                if indices[code] == "clear":
                    indices = LZW.__init_dict(min_lzw_code_size)
                    prev_indices = None
                    continue
                elif indices[code] == "end":
                    return result
                else:
                    for ind in indices[code]:
                        result.append(ind)
                    if prev_indices is not None:
                        indices[len(indices)] = prev_indices + [indices[code][0]]
            else:
                temp = indices[len(indices)] = prev_indices + [prev_indices[0]]
                result += temp
            prev_indices = indices[code]

    @staticmethod
    def __to_binary_string(data: bytes):
        result = ""
        for num in data:
            bin_data = str(bin(num))[2:]
            bin_data = ("0" * (8 - len(bin_data)) + bin_data)[::-1]
            # print(bin_data)
            result += bin_data
        return result

    @staticmethod
    def __init_dict(size: int):
        indices = {}
        for i in range(2 ** size):
            indices[i] = [i]
        indices[2 ** size] = "clear"
        indices[2 ** size + 1] = "end"

        return indices
