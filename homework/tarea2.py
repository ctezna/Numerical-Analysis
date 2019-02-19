from decimal import Decimal
# Class represents a new machine being made with a new number of bits, mantis, and exponents
class Bmachine():
    def __init__(self, bits, m, e):
        self.bits = bits
        self.m = m
        self.e = e
        self.max_num = 0
        self.eps = 0
        self.under = 0
        self.max_number()
        self.epsilon()
        self.underflow()

    def max_number(self):
        exp = [1] * self.e
        max_exp = 0
        max_root =  0
        for idx, val in enumerate(reversed(exp)):
            max_exp += (val * (2**idx))
        root_units = [1] * max_exp
        root_dec = [1] * (self.m + 1 - max_exp)
        root_units[self.m+1:] = [0] * (max_exp-self.m-1)
        for idx, val in enumerate(reversed(root_units)):
            max_root += (val * (2**idx))
        for idx, val in enumerate(root_dec):
            idx += 1
            idx *= -1
            max_root += (val * (2**(idx)))
        self.max_num = max_root
        return max_root
        
    def epsilon(self):
        exp = [1] * self.e
        eps_exp = 0
        eps_root = 0
        for idx, val in enumerate(reversed(exp)):
            eps_exp += (val * (2**idx))
        root_dec = [0] * (self.m + eps_exp + 1)
        root_dec[-1] = 1
        root_dec[eps_exp] = 1
        for idx, val in enumerate(root_dec):
            idx += 1
            idx *= -1
            eps_root += (val * (2**(idx)))
        self.eps = eps_root
        return eps_root
    
    def underflow(self):
        exp = [1] * self.e
        eps_exp = 0
        for idx, val in enumerate(reversed(exp)):
            eps_exp += (val * (2**idx))
        self.under = (2 ** (-1 * (eps_exp+1)))
        return self.under

    def machine_to_dec(self, machine):
        signM = int(machine[0])
        signE = int(machine[1])
        if signM == 0:
            signM = -1
        if signE == 0:
            signE = -1
        exp_bin = machine[2:self.e+2]
        root_bin = "1" + machine[self.e+2:self.m+self.e+2]
        root_bin = list(root_bin)
        mach_exp = 0
        result = 0
        for idx, val in enumerate(reversed(exp_bin)):
            mach_exp += (int(val) * (2**(idx)))
        mach_exp *= signE
        if mach_exp >= 0:
            root_units = root_bin[:mach_exp]
            root_dec = root_bin[mach_exp:]
        else:
            root_units = [0]
            root_dec = ([0] * abs(mach_exp)) + root_bin
        for idx, val in enumerate(reversed(root_units)):
            result += (int(val) * (2**idx))
        for idx, val in enumerate(root_dec):
            idx += 1
            idx *= -1
            result += (int(val) * (2**(idx)))
        return result
        


    def dec_to_machine(self, units, dec):
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
