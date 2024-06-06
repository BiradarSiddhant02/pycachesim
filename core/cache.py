from math import log2

class Block:
    def __init__(self, size: int):
        self.size = size
        self.t = 0
        self.v = 0
        self.d = 0
        self.data = [0 for i in range(int(log2(size)))]

class Set:
    def __init__(self, args):
        self.blocks = [Block(args.b) for i in range(int(log2(args.s // args.b // args.a)))]

class Cache:
    def __init__(self, args):
        self.byte_offset_len = int(log2(args.b))
        self.index_len = int(log2(args.s // args.b // args.a))
        self.tag_len = args.w - self.byte_offset_len - self.index_len 
        self.sets = [Set(args) for i in range(int(log2(args.s // args.b)))]