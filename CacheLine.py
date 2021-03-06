import logging

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
            logging.info("MISS %s", "(block not valid)" if block is not None else "")
            if self.write_allocation_strategy == 'a':
                self.replace(tag)
            return False
        else:
            logging.info("HIT")
            block.write(tag)
            self.increment_LRU_counters()
            return True

    def read(self, tag):
        block = self.get_block(tag)
        if block is None or not block.valid:
            logging.info("MISS")
            self.replace(tag)
            return False
        else:
            logging.info("HIT")
            block.read()
            self.increment_LRU_counters()
            return True

    def replace_LRU(self, tag):
        logging.info("performing an LRU replace")
        maxLRUblock = self.blocks[0]
        i=0
        for block in self.blocks:
            i+=1
            if block.LRU_counter > maxLRUblock.LRU_counter:
                maxLRUblock = block
            logging.info("block %d: LRU %d", i, block.LRU_counter)
        logging.info("Picked first block with counter %d", maxLRUblock.LRU_counter)
        maxLRUblock.write(tag)
        self.increment_LRU_counters()

    def replace_FIFO(self, tag):
        block = self.blocks[self.FIFO_index]
        block.write(tag)
        self.FIFO_index = (self.FIFO_index + 1) % len(self.blocks)

    def get_block(self, tag):
        for block in self.blocks:
            if block.tag == tag:
                return block
        return None

    def increment_LRU_counters(self):
        for block in self.blocks:
            block.LRU_counter += 1
