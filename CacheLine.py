from CacheBlock import CacheBlock


class CacheLine(object):
    def __init__(self, blocks, replacement_strategy, write_allocation_strategy):
        self.write_allocation_strategy = write_allocation_strategy
        self.blocks = [CacheBlock() for _ in range(blocks)]
        self.FIFO_index = 0

        if replacement_strategy == 'l':
            self.replace = self.replace_LRU
        elif replacement_strategy == 'f':
            self.replace = self.replace_FIFO
        else:
            raise ValueError("Not a valid replacement strategy")

    def write(self, tag):
        block = self.get_block(tag)
        if block is None or not block.valid:
            if self.write_allocation_strategy == 'a':
                self.replace(tag)
        else:
            block.write(tag)

    def read(self, tag):
        block = self.get_block(tag)
        if block is None or not block.valid:
            self.replace(tag)
        else:
            block.read()

    def replace_LRU(self, tag):
        maxLRUblock = self.blocks[0]
        for block in self.blocks:
            if block.LRU_counter > maxLRUblock.LRU_counter:
                maxLRUblock.LRU_counter += 1
                maxLRUblock = block
            else:
                block.LRU_counter += 1
        maxLRUblock.write(tag)

    def replace_FIFO(self, tag):
        block = self.blocks[self.FIFO_index]
        block.write(tag)
        self.FIFO_index = (self.FIFO_index + 1) % len(self.blocks)

    def get_block(self, tag):
        for block in self.blocks:
            if block.tag == tag:
                return block
        return None
