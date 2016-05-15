from consolehelper import consoleservice
from calculators import binary32calc
from calculators import binary64calc

BINARY32_FORMAT = 1
BINARY64_FORMAT = 2
FLOAT_REPR = 1
HEX_REPR = 2


INPUT_NUMBER = 'Input number-{0}:'
INPUT_OPERATION = 'Input operation(+, *, /):'


class InputProcesser:
    def __init__(self, number_format, number_repr, round_mode):
        self.__number_format = number_format
        self.__number_repr = number_repr
        self.__round_mode = round_mode

    @property
    def number_format(self):
        return self.__number_format

    @property
    def number_repr(self):
        return self.__number_repr

    @property
    def round_mode(self):
        return self.__round_mode

    @number_format.setter
    def number_format(self, number_format):
        self.__number_format = number_format

    @number_repr.setter
    def number_repr(self, number_repr):
        self.__number_repr = number_repr

    @round_mode.setter
    def round_mode(self, round_mode):
        self.__round_mode = round_mode

    def process(self):
        if self.number_format == BINARY32_FORMAT:
            res = self._binary32_processer()
            return res
        elif self.number_format == BINARY64_FORMAT:
            res = self._binary64_processer()
            return res

    def _binary32_processer(self):
        if self.number_repr == FLOAT_REPR:
            res = self.__float_bin32_processer()
            return res
        elif self.number_repr == HEX_REPR:
            res = self.__hex_bin32_processer()
            return res

    def _binary64_processer(self):
        if self.number_repr == FLOAT_REPR:
            res = self.__float_bin64_processer()
            return res
        elif self.number_repr == HEX_REPR:
            res = self.__hex_bin64_processer()
            return res

    def __float_bin32_processer(self):
        fst_num = consoleservice.ConsoleService.ask_float_num(INPUT_NUMBER.format('1'))
        snd_num = consoleservice.ConsoleService.ask_float_num(INPUT_NUMBER.format('2'))
        op = consoleservice.ConsoleService.ask_operator(INPUT_OPERATION)
        bin32_calc = binary32calc.Binary32Calc(fst_num, snd_num, self.number_repr, op, self.round_mode)
        res = bin32_calc.calculate()
        return (res, bin32_calc.exception_code)

    def __hex_bin32_processer(self):
        fst_num = consoleservice.ConsoleService.ask_hex32_num(INPUT_NUMBER.format('1'))
        snd_num = consoleservice.ConsoleService.ask_hex32_num(INPUT_NUMBER.format('2'))
        op = consoleservice.ConsoleService.ask_operator(INPUT_OPERATION)
        bin32_calc = binary32calc.Binary32Calc(fst_num, snd_num, self.number_repr, op, self.round_mode)
        res = bin32_calc.calculate()
        return (res, bin32_calc.exception_code)

    def __float_bin64_processer(self):
        fst_num = consoleservice.ConsoleService.ask_float_num(INPUT_NUMBER.format('1'))
        snd_num = consoleservice.ConsoleService.ask_float_num(INPUT_NUMBER.format('2'))
        op = consoleservice.ConsoleService.ask_operator(INPUT_OPERATION)
        bin64_calc = binary64calc.Binary64Calc(fst_num, snd_num, self.number_repr, op, self.round_mode)
        res = bin64_calc.calculate()
        return (res, bin64_calc.exception_code)

    def __hex_bin64_processer(self):
        fst_num = consoleservice.ConsoleService.ask_hex64_num(INPUT_NUMBER.format('1'))
        snd_num = consoleservice.ConsoleService.ask_hex64_num(INPUT_NUMBER.format('2'))
        op = consoleservice.ConsoleService.ask_operator(INPUT_OPERATION)
        bin64_calc = binary64calc.Binary64Calc(fst_num, snd_num, self.number_repr, op, self.round_mode)
        res = bin64_calc.calculate()
        return (res, bin64_calc.exception_code)
