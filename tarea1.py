# Autores: Carlos Tezna / Andres Pulgarin
import math, sys, time

def epsilon():
    x = float(1)
    while float(1) + float(x) != float(1):
        eps = x
        x = float(x) / float(2)
    return eps
start = time.time()
eps = epsilon()
end = time.time()
total = (end - start)
print("The machine epsilon is: " + str(eps))
print(" Evaluation took: " + str(total) + " sec" + "\n")

def max_num():
    x = 1e+10
    while not math.isinf(x) and x > 0:
        maxNum = x
        x = float(x) * float(10)
    while not math.isinf(maxNum) and maxNum > 0:
        maxx = maxNum
        maxNum *= (float(1.05))
    while not math.isinf(maxx) and maxx > 0:
        max2 = maxx
        maxx *= (float(1.00005))
    while not math.isinf(max2) and max2 > 0:
        max3 = max2
        max2 *= (float(1.00000001))
    while not math.isinf(max3) and max3 > 0:
        maxx_num = max3
        max3 *= (float(1.000000000001))
    return maxx_num

start = time.time()
maxx = max_num()
end = time.time()
total = (end - start)
print("The max number is: " + str(maxx))
print(" Evaluation took: " + str(total) + " sec" + "\n")
print("sys.float_info.max: " + str(sys.float_info.max))