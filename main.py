from floatprocesser import anyfloat
from consolehelper import consoleservice
from calculators import binary32calc
from calculators import binary64calc

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


def input_processer():
    # f = consoleservice.ConsoleService.ask_format_or_repr(CHOOSE_FORMAT)
    # r = consoleservice.ConsoleService.ask_format_or_repr(CHOOSE_REPR)
    # if r == 1:
    #     fst_num = consoleservice.ConsoleService.ask_bin32_num_in_bin_repr(INPUT_NUMBER.format('1'))
    # fst_num = consoleservice.ConsoleService.ask_num(INPUT_NUMBER.format('1'))
    # snd_num = consoleservice.ConsoleService.ask_num(INPUT_NUMBER.format('2'))
    # op = consoleservice.ConsoleService.ask_operation(INPUT_OPERATION)
    # if f == 1:
    #     bin32calc = binary32calc.Binary32Calc(fst_num, snd_num, r, op)
    #     bin32calc.calculate()
    # elif f == 2:
    #     bin64calc = binary64calc.Binary64Calc(fst_num, snd_num, r, op)
    #     bin64calc.calculate()

    print(anyfloat.AnyFloat._decode())


def main():
    input_processer()
    n = int('00111110001000000000000000000000', 2)
    k = int('00000000000010000000000000000000', 2)
    nf = anyfloat.AnyFloat.from_ieee(n, (8, 23))
    kf = anyfloat.AnyFloat.from_ieee(k, (8, 23))
    print(float(anyfloat.AnyFloat.from_float(23.34)))

if __name__ == '__main__':
    main()
