from math import log2

class Block:
    def __init__(self, size: int):
        self.size = size  # Size of the block (number of data elements it can hold)
        self.t = 0  # Tag
        self.v = 0  # Valid bit
        self.d = 0  # Dirty bit
        self.data = [0 for _ in range(size)]  # Data storage for the block

    def __getitem__(self, idx):
        return self.data[idx]  # Access data using index

    def __setitem__(self, idx, value):
        self.data[idx] = int(value) // 0xff  # Modify data using index, only one byte

    def __len__(self):
        return self.size  # Overload len() to return the size of the block

    def __repr__(self):
        return f"Block(size={self.size}, t={self.t}, v={self.v}, d={self.d}, data={self.data})"

    def __str__(self):
        return ' '.join(f"{byte:02x}".upper() for byte in self.data)

class Set:
    def __init__(self, num_blocks: int, block_size: int):
        self.blocks = [Block(block_size) for _ in range(num_blocks)]

    def __getitem__(self, idx):
        return self.blocks[idx]  # Access blocks using index

    def __setitem__(self, value, idx=0):
        self.blocks[idx] = value  # Modify blocks using index

    def __len__(self):
        return len(self.blocks)  # Overload len() to return the number of blocks in the set

    def __repr__(self):
        return f"Set(blocks={self.blocks})"

    def __str__(self):
        return '\n'.join(str(block) for block in self.blocks)

class Cache:
    def __init__(self, args):
        self.byte_offset_len = int(log2(args.b))  # Length of the byte offset
        self.index_len = int(log2(args.s // args.b // args.a))  # Length of the index
        self.tag_len = args.w - self.byte_offset_len - self.index_len  # Length of the tag
        num_sets = args.s // (args.b * args.a)
        self.sets = [Set(args.a, args.b) for _ in range(num_sets)]  # List of sets in the cache

    def __getitem__(self, idx):
        return self.sets[idx]  # Access sets using index

    def __setitem__(self, idx, value):
        self.sets[idx] = value  # Modify sets using index

    def __len__(self):
        return len(self.sets)  # Overload len() to return the number of sets in the cache

    def __repr__(self):
        return f"Cache(sets={self.sets})"

    def __str__(self):
        return '\n'.join(f"{cache_set}" for cache_set in self.sets)