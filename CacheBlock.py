class CacheBlock(object):
    def __init__(self):
        self.valid = False
        self.tag = 0
        self.LRU_counter = 0

    def write(self, tag):
        self.tag = tag
        self.valid = True
        self.LRU_counter = 0

    def read(self):
        self.LRU_counter = 0