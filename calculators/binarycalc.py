from abc import abstractclassmethod


class BinaryCalc:
    def __init__(self, first_num, second_num, rep_num, operation):
        self.__first_num = first_num
        self.__second_num = second_num
        self.__rep_num = rep_num
        self.__operation = operation

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

    def calculate(self):
        res = 0
        if self.rep_num == 1:
            res = self._binary_calculator()
        elif self.rep_num == 2:
            res = self._anyfloat_calculator()
        return res

    @abstractclassmethod
    def _binary_calculator(self):
        pass

    @abstractclassmethod
    def _anyfloat_calculator(self):
        pass