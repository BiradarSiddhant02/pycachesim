import numpy as np

class Memory:

    def __init__(self, size: int):
        self.size = size
        self.len = 32
        self.data = np.array([["0x"+(hex(np.random.randint(0x00, 0xff)))[2:].zfill(len // 16)\
                               for i in range(size // len // 4)] for j in range(size // len)])


    def __str__(self):
        repr = str()
        for block in self.data:
            for byte in block:
                repr = repr + byte + " "
            repr = repr + "\n"

        return repr