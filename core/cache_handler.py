from typing import Tuple
from math import log2

class CacheHandler:
    def __init__(self, cache, memory):
        self.cache = cache
        self.memory = memory


    def translate_addr(self, addr: str) -> Tuple[int, int, int]:
        try:
            # check if input is in binary or hexadecimal
            if addr[:2] == '0b' or all(char in "01" for char in addr):
                address = int(addr[2:], 2) if addr[:2] == '0b' else int(addr, 2)
            elif addr[:2] == '0x' or all(char in "0123456789abcdef" for char in addr.lower()):
                address = int(addr[2:], 16) if addr[:2] == '0x' else int(addr, 16)
            else:
                raise ValueError("Invalid address format")

            # extract the block and byte to be extracted
            byte_field_mask = (1 << self.cache.byte_offset_len) - 1
            index_field_mask = ((1 << (self.cache.index_len)) - 1) << self.cache.byte_offset_len
            tag_field_mask = ((1 << (8 - self.cache.byte_offset_len - self.cache.index_len)) - 1) << (self.cache.byte_offset_len + self.cache.index_len)

            byte_field = address & byte_field_mask
            index_field = (address & index_field_mask) >> self.cache.byte_offset_len
            tag_field = (address & tag_field_mask) >> (self.cache.byte_offset_len + self.cache.index_len)

            return tag_field, index_field, byte_field

        except ValueError:
            print("Error: Invalid input value")


    def update_cache(self, data: int, block: int) -> int:
        pass

    def read_byte(self, loc: tuple) -> int:
        pass

    def write_byte(self, byte: int, loc: tuple) -> int:
        pass
