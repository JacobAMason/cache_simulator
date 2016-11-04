# Cache Simulator
This is a simple Dinero Cache Simulator written in Python for a project in my Computer Architecture course.

It is written in Python 2 to be compatible with a test runner that was included with the assignment.

The simulator is divided into three modules, `Cache`, `CacheLine`, and `CacheBlock`.

`CacheBlock` contains a valid bit, tag information, and an LRU counter for the Least-Recently-Used method of block replacement. The two methods allow for easy reading and writing simulation. The block is unaware of its location in the cache.

`CacheLine` simulates a line of cache. Like the block, it is unaware of its index. It is, however, aware of the replacement strategy, and it determines whether a hit or a miss occurs on any given cache operation. The `CacheLine` has two public functions, write and read, just like the block.

`Cache` is the "root" module. It has helper functions to calculate the cache line, the tag, and the block address from an address. Just like the `CacheLine` and `CacheBlock`, it offers two key methods, read and write. There is a simple simulation method that will operate on a file passed when the object is constructed. Example files (called traces) are in the `traces` folder.
