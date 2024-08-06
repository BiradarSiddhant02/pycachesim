from collections import OrderedDict
import numpy as np
from math import log2

class Cache:
    # aarch: system architecture (32bit, 64bit)
    # associativity: cache associativity
    # size: cache size
    # replacement: cache block replacement protocol
    def __init__(self, associativity = 1, size = 1024, aarch = 32, replacement = "lru"):
        self.size = size
        self.line_size = aarch // 8     # in bytes
        self.set_size = (aarch // 8) * associativity

        self.cache = [OrderedDict() for _ in range(size // associativity)]

    def __getitem__(self, addr: int) -> int:
         
