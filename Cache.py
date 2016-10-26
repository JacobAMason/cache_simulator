from CacheLine import CacheLine


class Cache(object):
    def __init__(self, fname, usize, ubsize, uassoc, urepl, uwalloc):
        self.fname = fname
        self.cacheSize = usize
        self.blockSize = ubsize
        self.associativity = uassoc
        self.replacementStrategy = urepl
        self.writeAllocationStrategy = uwalloc
        self.numCacheLines = self.cacheSize // (self.associativity * self.blockSize)
        self.cacheLines = [CacheLine(self.associativity, self.replacementStrategy, self.writeAllocationStrategy) for _ in range(self.numCacheLines)]

    def dosim(self):
        print "Number of cache lines is:", self.numCacheLines
        self.numMisses = 0
        numAccesses = 0
        with open(self.fname) as din:
            for line in din:
                line = line.split()
                label = int(line[0])
                address = int(line[1], 16)
                if label == 0 or label == 2:
                    self.read(address)
                elif label == 1:
                    self.write(address)
                else:
                    raise ValueError("Unknown label: " + line[0])
                numAccesses += 1
        return self.numMisses, numAccesses

    def read(self, address):
        cacheLine = self.get_cache_line(address)
        tag = self.get_tag(address)
        cacheLine.read(tag)

    def write(self, address):
        cacheLine = self.get_cache_line(address)
        tag = self.get_tag(address)
        cacheLine.write(tag)

    def get_cache_line(self, address):
        block_address = self.get_block_address(address)
        return self.cacheLines[block_address % self.numCacheLines]

    def get_tag(self, address):
        return address // (self.numCacheLines * self.blockSize)

    def get_block_address(self, address):
        return address // self.blockSize
