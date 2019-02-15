from decimal import Decimal
# Class represents a new machine being made with a new number of bits, mantis, and exponents
class Bmachine():
    def __init__(self, bits, m, e):
        self.bits = bits
        self.m = m
        self.e = e
        self.max_num = 0

    def max_number(self):
        root = [1] * self.m
        exp = [1] * self.e
        max_root = 0
        max_exp = 0
        for idx, val in enumerate(reversed(root)):
            max_root += (val * (2**idx))
        for idx, val in enumerate(exp):
            max_exp += (val * (2**idx))
        max_num = max_root * (10 ** max_exp)
        self.max_num = max_num
        max_num = '%.10E' % Decimal(str(max_num))
        return max_num

    def epsilon(self):
        root = [0] * self.m
        root[self.m-1] = 1
        exp = [1] * self.e
        eps_root = 0
        eps_exp = 0
        for idx, val in enumerate(reversed(root)):
            eps_root += (val * (2**idx))
        for idx, val in enumerate(exp):
            eps_exp += (val * (2**idx))
        eps_exp *= -1
        eps = eps_root * (10 ** eps_exp)
        return eps

def userInput():
    print("input # of bits for mantis (m): ")
    mantis = int(input())
    print("input # of bits for exponent (e): ")
    exp = int(input())
    bm = Bmachine((mantis + exp + 2), mantis, exp)
    print()
    print("You have created a new machine with {} bits, {} designated for the mantis and {} designated for the exponents.".format(bm.bits,bm.m,bm.e))
    print()
    print("Max Number (Scientific Notation*): ".upper(), bm.max_number())
    print("*Rounded simetrically to 10 decimal places")
    print("Max Number (Normal): ".upper(), bm.max_num)
    print("Epsilon: ".upper(), bm.epsilon())
    print("Press 0 to quit, Press enter to continue")

while True:
    userInput()
    try:
        if int(input()) == 0:
            break
    except ValueError:
        pass