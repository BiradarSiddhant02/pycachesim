import numpy as np

class Memory:

    def __init__(self, size: int):
        self.size = size
        self.block_size = 32
        self.data = np.array([["0x"+(hex(np.random.randint(0x00, 0xff)))[2:].zfill(self.block_size // 16)\
                               for i in range(size // self.block_size // 4)] for j in range(size // self.block_size)])


    def __str__(self):
        repr = str()
        for block in self.data:
            for byte in block:
                repr = repr + byte + " "
            repr = repr + "\n"

        return repr
