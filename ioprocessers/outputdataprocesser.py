from consolehelper import consoleservice
from softfloat import bits32tofloat, bits64tohex, bits64tofloat
from ioprocessers import inputdataprocesser


class OutputProcesser:
    def __init__(self, res, exception_code, number_format):
        self.__res = res
        self.__exception_code = exception_code
        self.__number_format = number_format

    @property
    def res(self):
        return self.__res

    @property
    def exception_code(self):
        return self.__exception_code

    @property
    def number_format(self):
        return self.__number_format

    @res.setter
    def res(self, res):
        self.__res = res

    @exception_code.setter
    def exception_code(self, exception_code):
        self.__exception_code = exception_code

    @number_format.setter
    def number_format(self, number_format):
        self.__number_format = number_format

    def process(self):
        if self.number_format == inputdataprocesser.BINARY32_FORMAT:
            consoleservice.ConsoleService.print_message('Result in HEX format: ' + hex(self.res))
            consoleservice.ConsoleService.print_message('Result in Float format: ' + str(bits32tofloat(self.res)))
            consoleservice.ConsoleService.print_message('Exception mask: ' + bin(self.exception_code))
        elif self.number_format == inputdataprocesser.BINARY64_FORMAT:
            consoleservice.ConsoleService.print_message('Result in HEX format: ' + hex(bits64tohex(self.res)))
            consoleservice.ConsoleService.print_message('Result in Float format: ' + str(bits64tofloat(self.res)))
            consoleservice.ConsoleService.print_message('Exception mask: ' + bin(self.exception_code))
