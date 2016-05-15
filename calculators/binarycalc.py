from abc import abstractclassmethod


class BinaryCalc:
    def __init__(self, first_num, second_num, rep_num, operation, round_mode):
        self.__first_num = first_num
        self.__second_num = second_num
        self.__rep_num = rep_num
        self.__operation = operation
        self.__round_mode = round_mode
        self.__exception_code = 0

    @property
    def first_num(self):
        return self.__first_num

    @property
    def second_num(self):
        return self.__second_num

    @property
    def rep_num(self):
        return self.__rep_num

    @property
    def operation(self):
        return self.__operation

    @property
    def round_mode(self):
        return self.__round_mode

    @property
    def exception_code(self):
        return self.__exception_code

    @first_num.setter
    def first_num(self, first_num):
        self.__first_num = first_num

    @second_num.setter
    def second_num(self, second_num):
        self.__second_num = second_num

    @rep_num.setter
    def rep_num(self, rep_num):
        self.__rep_num = rep_num

    @operation.setter
    def operation(self, operation):
        self.__operation = operation

    @round_mode.setter
    def round_mode(self, round_mode):
        self.__round_mode = round_mode

    @exception_code.setter
    def exception_code(self, exception_code):
        self.__exception_code = exception_code

    def calculate(self):
        res = 0
        if self.rep_num == 1:
            res = self._float_calculator()
        elif self.rep_num == 2:
            res = self._hex_calculator()
        return res

    @abstractclassmethod
    def _float_calculator(self):
        pass

    @abstractclassmethod
    def _hex_calculator(self):
        pass
