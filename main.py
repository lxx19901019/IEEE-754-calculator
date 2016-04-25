from consolehelper import consoleservice
from ioprocessers import inputdataprocesser
from ioprocessers import outputdataprocesser

# from math import exp
# n = int('00111110001000000000000000000000', 2)
# k = int('00000000000010000000000000000000', 2)
# nf = anyfloat.anyfloat.from_ieee(n, (8, 23))
# kf = anyfloat.anyfloat.from_ieee(k, (8, 23))
# print(anyfloat.anyfloat.from_float(23.34))

CHOOSE_FORMAT = 'Choose a format of numbers for calculation: (1)binary32 or (2)binary64:'
CHOOSE_REPR = 'Choose a representation of numbers:\n' \
                 '(1)Binary\n' \
                 '(2)Anyfloat(sign=<0,1>,exponent=<[0;2^8-1]>/<[0;2^11-1]>,significand=<[0;2^23-1]>/<[0;2^52-1]>)\n' \
                 '(3)HEX(without "0x" prefix):'


def main():
    try:
        f = consoleservice.ConsoleService.ask_format(CHOOSE_FORMAT)
        r = consoleservice.ConsoleService.ask_repr(CHOOSE_REPR)
        in_proc = inputdataprocesser.InputProcesser(f, r)
        out_proc = outputdataprocesser.OutputProcesser(in_proc.process())
        out_proc.process()
    except:
        consoleservice.ConsoleService.print_message('\nBye!')


def test():
    from floatprocesser import anyfloat
    n = int('0011111111000100000000000000000001000000000000000000000000000000', 2)# 0.1562500298023224
    a = anyfloat.AnyFloat.from_ieee(int('3cc80005', 16), (8, 23))# 0.024414071813226634 0x3f990000a0000100
    print(float(a))

if __name__ == '__main__':
    # test()
    main()
