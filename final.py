from call import *
from time import sleep

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    block = blockInput()
    block.block()
    sleep(5)

    block.unblock()
    
