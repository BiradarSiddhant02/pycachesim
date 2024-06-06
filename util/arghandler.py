import argparse
import sys

class ArgHandler:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="-w <address width> -s <cache size> -b <block size> \
                                     -a <associativity> -wh <write-hit> -wm <write miss> -r <replacement>")
        self.parser.add_argument("-w", type=int, default=32, help="address width")
        self.parser.add_argument("-s", type=int, default=1024, help="cache size")
        self.parser.add_argument("-b", type=int, default=8, help="block size")
        self.parser.add_argument("-a", type=int, default=1, help="associativity")
        self.parser.add_argument("-wh", type=str, default="wb", help="write hit procedure")
        self.parser.add_argument("-wm", type=str, default="wa", help="write miss procedure")
        self.parser.add_argument("-r", type=str, default="lru", help="replacement procedure")

    def parse_arguments(self):
        args = self.parser.parse_args(sys.argv[1:])
        return args

    def validate_arguments(self, args):
        addr_wd = args.w        # address width
        cach_sz = args.s        # cache size
        blck_sz = args.b        # block size
        assoc   = args.a        # associativity
        wrte_ht = args.wh       # write hit protocol
        wrte_ms = args.wm       # write miss protocol
        rplcmnt = args.r        # replacement protocol

        valid_width = addr_wd in [4, 6, 8, 10, 12]
        valid_csize = cach_sz in [8, 16, 32, 64, 128, 256]
        valid_bsize = blck_sz in [2, 4, 8]
        valid_assoc = assoc in [1, 2, 4]
        valid_wh = wrte_ht in ["wb", "wt"]
        valid_wm = wrte_ms in ["wa", "nwa"]
        valid_rplcmnt = rplcmnt in ["lru", "rnd", "fifo"]

        if not (valid_width and valid_csize and valid_bsize and valid_assoc and valid_wh and valid_wm and valid_rplcmnt):
            print("Warning: One or more arguments are invalid. Reverting to default values.")
            args.w = 8
            args.s = 64
            args.b = 8
            args.a = 1
            args.wh = "wb"
            args.wm = "wa"
            args.r = "lru"

        return args
    
    def print_arguments(self, validated_args):
        print("Address Width:", validated_args.w)
        print("Cache Size:", validated_args.s)
        print("Block Size:", validated_args.b)
        print("Associativity:", validated_args.a)
        print("Write Hit Protocol:", validated_args.wh)
        print("Write Miss Protocol:", validated_args.wm)
        print("Replacement Protocol:", validated_args.r)