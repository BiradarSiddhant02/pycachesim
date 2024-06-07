from util.arghandler import ArgHandler
from core.cache import Cache
from core.memory import Memory
from core.cache_handler import CacheHandler

if __name__ == "__main__":
    arg_handler = ArgHandler()
    args = arg_handler.parse_arguments()
    validated_args = arg_handler.validate_arguments(args)
    # arg_handler.print_arguments(validated_args)

    cache = Cache(validated_args)
    memory = Memory(validated_args.s)

    c_handler = CacheHandler(cache, memory)


    # cache.print_cache()
    cache[1][0][1] = 10
    cache[1][0][3] = 256
    print(cache)





    # tag, ind, byte = c_handler.translate_addr("0x10")
    # print(bin(tag), bin(ind), bin(byte))
    # tag, ind, byte = c_handler.translate_addr("0x30")
    # print(bin(tag), bin(ind), bin(byte))
    # tag, ind, byte = c_handler.translate_addr("0x0a")
    # print(bin(tag), bin(ind), bin(byte))
    # tag, ind, byte = c_handler.translate_addr("0xa4")
    # print(bin(tag), bin(ind), bin(byte))



