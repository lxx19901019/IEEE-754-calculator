class Calculator:
    def __init__(self, lhs, rhs, operation):
        self.__lhs = lhs
        self.__rhs = rhs
        self.__operation = operation

    @property
    def lhs(self):
        return self.__lhs

    @property
    def rhs(self):
        return self.__rhs

    @property
    def operation(self):
        return self.__operation

    @lhs.setter
    def lhs(self, lhs):
        self.__lhs = lhs

    @rhs.setter
    def rhs(self, rhs):
        self.__rhs = rhs

    @operation.setter
    def operation(self, operation):
        self.__operation = operation

    def calculate(self):
        if self.operation == '+':
            return self._sum()
        if self.operation == '*':
            return self._multiply()
        if self.operation == '/':
            return self._div()

    def _sum(self):
        return self.lhs + self.rhs

    def _multiply(self):
        return self.lhs * self.rhs

    def _div(self):
        return self.lhs / self.rhs
