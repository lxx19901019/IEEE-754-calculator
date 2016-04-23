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
CHOOSE_REPR = 'Choose a representation of numbers: ' \
                 '(1)Binary or ' \
                 '(2)Anyfloat(sign=<0,1>,exponent=<[0;2^8-1]>/<[0;2^11-1]>,significand=<[0;2^23-1]>/<[0;2^52-1]>):'


def main():
    try:
        f = consoleservice.ConsoleService.ask_format_or_repr(CHOOSE_FORMAT)
        r = consoleservice.ConsoleService.ask_format_or_repr(CHOOSE_REPR)
        in_proc = inputdataprocesser.InputProcesser(f, r)
        out_proc = outputdataprocesser.OutputProcesser(in_proc.process())
        out_proc.process()
    except:
        consoleservice.ConsoleService.print_message('\nError! Try again!')


def test():
    from floatprocesser import anyfloat
    n = int('00111110001000000000000000000000', 2)
    k = int('00000000000010000000000000000000', 2)
    nf = anyfloat.AnyFloat.from_ieee(n, (8, 23))
    kf = anyfloat.AnyFloat.from_ieee(k, (8, 23))
    print(float(nf))
    print(nf.bin((8, 23)))

if __name__ == '__main__':
    test()
    # main()
