import numpy as np

class Memory:
    def __init__(self, size: int):
        self.size = size    # in bytes
        self.block_size = 4 # in bytes
        self.num_blocks = self.size // self.block_size
        self.data = np.array(np.random.randint(0, 0xff, (self.num_blocks, self.block_size), np.uint8))

    def __str__(self):
        result = []
        for i, block in enumerate(self.data):
            block_address = self._get_addr(i * 8) # to print the address of the line in memory
            result.append(f'{block_address}: ' + ' '.join(f'{byte:02x}' for byte in block))
        return '\n'.join(result)
    
    def __getitem__(self, addr):
        # Convert the address to an integer
        addr = int(addr, 16)
        # Calculate block number and offset within the block
        block_num = addr // self.block_size
        offset = addr % self.block_size
        # Retrieve the byte from the block
        return self.data[block_num][offset]

    @staticmethod
    def _get_addr(number: int) -> str:
        return f'{number:04x}'


