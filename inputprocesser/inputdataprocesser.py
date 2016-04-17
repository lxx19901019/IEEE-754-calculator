from consolehelper import consoleservice
from calculators import binary32calc
from calculators import binary64calc

BINARY32_FORMAT = 1
BINARY_REPR = 1
BINARY64_FORMAT = 2
ANYFLOAT_REPR = 2


INPUT_NUMBER = 'Input number-{0}:'
INPUT_OPERATION = 'Input operation(+, *, /):'
INPUT_SIGN_NUM = 'Input "1" if sign is "+" and "0" if sign is "-"'
INPUT_EXPONENT32 = 'Input exponent for 32 binary anyfloat number'
INPUT_SIGNIFICAND32 = 'Input significand for 32 binary anyfloat number'
INPUT_EXPONENT64 = 'Input exponent for 64 binary anyfloat number'
INPUT_SIGNIFICAND64 = 'Input significand for 64 binary anyfloat number'


class InputProcesser:
    def __init__(self, number_format, number_repr):
        self.__number_format = number_format
        self.__number_repr = number_repr

    @property
    def number_format(self):
        return self.__number_format

    @property
    def number_repr(self):
        return self.__number_repr

    @number_format.setter
    def number_format(self, number_format):
        self.__number_format = number_format

    @number_repr.setter
    def number_repr(self, number_repr):
        self.__number_repr = number_repr

    def process(self):
        if self.number_format == BINARY32_FORMAT:
            self._binary32_processer()
        elif self.number_format == BINARY64_FORMAT:
            self._binary64_processer()

    def _binary32_processer(self):
        if self.number_repr == BINARY_REPR:
            self.__binary_bin32_processer()
        elif self.number_repr == ANYFLOAT_REPR:
            self.__anyfloat_bin32_processer()
        pass

    def _binary64_processer(self):
        if self.number_repr == BINARY_REPR:
            self.__binary_bin64_processer()
        elif self.number_repr == ANYFLOAT_REPR:
            self.__anyfloat_bin64_processer()
        pass

    def __binary_bin32_processer(self):
        fst_num = consoleservice.ConsoleService.ask_bin32_num_in_bin_repr(INPUT_NUMBER.format('1'))
        snd_num = consoleservice.ConsoleService.ask_bin32_num_in_bin_repr(INPUT_NUMBER.format('2'))
        op = consoleservice.ConsoleService.ask_operator(INPUT_OPERATION)
        bin32_calc = binary32calc.Binary32Calc(fst_num, snd_num, self.number_repr, op)

    def __anyfloat_bin32_processer(self):
        fst_num = consoleservice.ConsoleService.ask_anyfloat32_num(INPUT_SIGN_NUM, INPUT_EXPONENT32, INPUT_EXPONENT32)
        snd_num = consoleservice.ConsoleService.ask_anyfloat32_num(INPUT_SIGN_NUM, INPUT_EXPONENT32, INPUT_EXPONENT32)
        op = consoleservice.ConsoleService.ask_operator(INPUT_OPERATION)
        bin32_calc = binary32calc.Binary32Calc(fst_num, snd_num, self.number_repr, op)

    def __binary_bin64_processer(self):
        fst_num = consoleservice.ConsoleService.ask_bin64_num_in_bin_repr(INPUT_NUMBER.format('1'))
        snd_num = consoleservice.ConsoleService.ask_bin64_num_in_bin_repr(INPUT_NUMBER.format('2'))
        op = consoleservice.ConsoleService.ask_operator(INPUT_OPERATION)
        bin64_calc = binary64calc.Binary64Calc(fst_num, snd_num, self.number_repr, op)

    def __anyfloat_bin64_processer(self):
        fst_num = consoleservice.ConsoleService.ask_anyfloat64_num(INPUT_SIGN_NUM, INPUT_EXPONENT64, INPUT_EXPONENT64)
        snd_num = consoleservice.ConsoleService.ask_anyfloat64_num(INPUT_SIGN_NUM, INPUT_EXPONENT64, INPUT_EXPONENT64)
        op = consoleservice.ConsoleService.ask_operator(INPUT_OPERATION)
        bin32_calc = binary64calc.Binary64Calc(fst_num, snd_num, self.number_repr, op)
