from consolehelper import consoleservice
from floatprocesser import anyfloat


SINGLE_PRECISION_HEX_FORMAT = 'num in single precision, in hex format: {0}'
SINGLE_PRECISION_FLOAT_FORMAT = 'num in single precision, in float format: {0}'
DOUBLE_PRECISION_HEX_FORMAT = 'num in double precision, in hex format: {0}'
DOUBLE_PRECISION_FLOAT_FORMAT = 'num in double precision, in float format: {0}'
SINGLE_PRECISION = (8, 23)
SINGLE = '1'
DOUBLE = '2'


class OutputProcesser:
    def __init__(self, res):
        self.__res = res

    @property
    def res(self):
        return self.__res

    @res.setter
    def res(self, res):
        self.__res = res

    def process(self):
        consoleservice.ConsoleService.print_message(SINGLE_PRECISION_HEX_FORMAT.format(str(hex(self.res.to_ieee(SINGLE_PRECISION)))))
        a = anyfloat.AnyFloat.from_ieee(int(str(hex(self.res.to_ieee(SINGLE_PRECISION))), 16), SINGLE_PRECISION)
        consoleservice.ConsoleService.print_message(SINGLE_PRECISION_FLOAT_FORMAT.format(str(float(a))))
        consoleservice.ConsoleService.print_message(DOUBLE_PRECISION_HEX_FORMAT.format(str(hex(self.res.to_ieee()))))
        consoleservice.ConsoleService.print_message(DOUBLE_PRECISION_FLOAT_FORMAT.format(str(float(self.res))))
