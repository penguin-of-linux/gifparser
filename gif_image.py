import gif_parser
import logical_screen_descriptor
import color_table
import Block.image_descriptor as ids
import Block.image_block as ib


class GifImage:
    def __init__(self, data: bytes):
        self.logical_screen_descriptor = None
        self.global_color_table = None
        self.frames = []

        blocks = gif_parser.GifParser.parse_all(data)

        for i, block in enumerate(blocks):
            if isinstance(block, logical_screen_descriptor.LSD):
                self.logical_screen_descriptor = block

            if isinstance(block, ids.ImageDescriptor):
                if block.local_color_table_flag:
                    self.frames.append(Frame(block, blocks[i+1], blocks[i+2]))
                else:
                    self.frames.append(Frame(block, self.global_color_table, blocks[i+1]))
            if isinstance(block, color_table.ColorTable):
                self.global_color_table = block


class Frame:
    def __init__(self, descriptor: ids.ImageDescriptor, table: color_table.ColorTable, image_block: ib.ImageBlock):
        self.descriptor = descriptor
        self.color_table = table
        self.image_block = image_block
