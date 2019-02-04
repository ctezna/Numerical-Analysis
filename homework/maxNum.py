#Nicolas Gonzalez Vallejo

import sys
def maxNum():
    d = 0.5
    res = 0
    while d < float('inf'):
        if d > res:
            res=d
            print(res)
        d *= 2
    print(res*1.9999999999999998)
    print("sys: ", sys.float_info.max)

maxNum()