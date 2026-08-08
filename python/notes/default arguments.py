# default arguments = A default value for certain parameters.
#                         default is used when that argument is omitted
#                         make your function more flexible , reduces number of arguments
#                 1. positional   2. DEFAULT  3. keyword,  4. arbitrary
from more_itertools.more import doublestarmap


def net_price(price, discount= 0, tax= 0.18):                   #these parameters with "=" denotes their default values
    return (price - (price*discount))*(tax + 1)

print(net_price(500,0, 0.18))
print(net_price(500))                                           #so therefore, the empty goin arguments will take the value of default armuments
print(net_price(500,0.1,0))


import time

def count(end,start= 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done !")


count(15)


