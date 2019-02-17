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


    def dec_to_machine(self, units, dec): # It's still incomplete
        dec_number = dec
        sig_exp = ""
        mant = ""
        sig_mant = ""
        units = str(units)
        dec = self.dec_to_bin(dec, 10)
        units = bin(int(units))[2:]
        number = "%s.%s" % (units, dec)
        pos_point = len(units)
        if units[0] == "1":
            exp = pos_point
            sig_exp = "1"
        else:
            mant_aux = units + dec
            exp = mant_aux.index("1") - 1
            print (exp)
            sig_exp = "0"

        sig_mant = "0" if float(number) < 0 else "1"
        #Condiciones para controlar el exponente
        exp_bin = bin(exp)[2:]
        if len(exp_bin) < self.e:
            exp_bin = "0" * (self.e - len(exp_bin))  + exp_bin 
        elif len(exp_bin) > self.e:
            exp_bin = exp_bin[:len(exp_bin) - self.e]

        #Condiciones para controlar la mantiza
        if len(units) - 1 == self.m:
            mant = units[1:]
        elif len(units) - 1 > self.m:
            mant = units[1:self.m - len(units)]
        else:
            mant = units[1:] + self.dec_to_bin(dec_number, self.m-(len(units) - 1))



        print("units: " + units)
        print("dec: " + dec)
        print("sig_mant: " + sig_mant)
        print("sig_exp: " + sig_exp)
        print("exp_bin: " + exp_bin)
        print("mant: " + mant)

        return sig_mant + sig_exp + exp_bin + mant


    def dec_to_bin(self, dec, rang):
        bin_dec = ""
        number = "0.%s" % (str(dec))

        for digit in range(rang):
            mult = float(number) * 2
            mult = str(mult)
            bin_dec += mult[0]

            if float(mult) >= 1:
                index = mult.index(".")
                number = "0.%s" % mult[index + 1:]
            else:
                number = mult

        return bin_dec



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
    #print("prueba: " + bm.dec_to_bin(40, 5))
    print("Number: " + str(bm.dec_to_machine(0,23)))
    print("Press 0 to quit, Press enter to continue")


while True:
    userInput()
    try:
        if int(input()) == 0:
            break
    except ValueError:
        pass
