import lib
import config
from keyboard import write
from time import sleep
import random

lis = lib.main()

num = int(input('select message > '))

sleep(config.wait)



if num == 0:
    for i in lis:
        write(f'{i}\n', delay=config.delay)
        sleep(config.sleep)

else:
    for i in range(num):
        x = random.randint(0,len(lis)-1)
        write(f"{lis[x]}\n", delay=config.delay)
        sleep(config.sleep)

