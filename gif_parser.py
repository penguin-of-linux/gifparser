import Block.ExtensionBlock.application_extension as ae
import Block.ExtensionBlock.comment_extension as ce
import Block.ExtensionBlock.extension_block as eb
import Block.ExtensionBlock.graphic_manage_extension as eg
import Block.ExtensionBlock.plain_text_extension as pe
import Block.block
import Block.image_descriptor
import color_table
import header
import logical_screen_descriptor
import gif_image

from Block import image_block


class GifParser:
    @staticmethod
    def get_header(data: bytes):
        return header.Header(data[:6])

    @staticmethod
    def get_logical_screen_descriptor(data: bytes):
        return logical_screen_descriptor.LSD(data)

    @staticmethod
    def get_global_color_table(data: bytes, size: int):
        return color_table.ColorTable(data, 13, size)

    @staticmethod
    def get_block(data: bytes, pos: int):
        result = None

        block_code = data[pos]
        pos += 1
        extension_code = data[pos]

        if block_code == eb.ExtensionBlock.block_code:
            if extension_code == eg.GraphicManageExtension.extension_code:
                result = eg.GraphicManageExtension(data, pos)
            if extension_code == ae.ApplicationExtension.extension_code:
                result = ae.ApplicationExtension(data, pos)
            if extension_code == ce.CommentExtension.extension_code:
                result = ce.CommentExtension(data, pos)
            if extension_code == pe.PlainTextExtension.extension_code:
                result = pe.PlainTextExtension(data, pos)

            # debug
            # print("ext code: " + str(extension_code))

        if block_code == Block.image_descriptor.ImageDescriptor.block_code:
            result = Block.image_descriptor.ImageDescriptor(data, pos)

        return result

    @staticmethod
    def parse_all(data: bytes):
        blocks = []

        head = GifParser.get_header(data)
        blocks.append(head)

        lsd = GifParser.get_logical_screen_descriptor(data)
        blocks.append(lsd)

        i = 13
        if lsd.global_color_table_using:
            gct = GifParser.get_global_color_table(data, lsd.global_color_table_size)
            blocks.append(gct)
            i += len(gct)

        while i < len(data) - 1:
            block = GifParser.get_block(data, i)
            if block is not None:
                blocks.append(block)
                i += len(block)
                if isinstance(block, Block.image_descriptor.ImageDescriptor):
                    if block.local_color_table_flag:
                        lct = color_table.ColorTable(data, i, block.local_color_table_size)
                        blocks.append(lct)
                        i += len(lct)
                    image = image_block.ImageBlock(data, i)
                    blocks.append(image)
                    i += len(image)
            i += 1

        return blocks
