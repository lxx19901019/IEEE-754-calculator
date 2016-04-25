from calculators import binarycalc
from calculators import calculator
from floatprocesser import anyfloat


class Binary64Calc(binarycalc.BinaryCalc):
    def _binary_calculator(self):
        lhs = anyfloat.AnyFloat.from_ieee(int(self.first_num, 2))
        rhs = anyfloat.AnyFloat.from_ieee(int(self.second_num, 2))
        calc = calculator.Calculator(float(lhs), float(rhs), self.operation)
        res = calc.calculate()
        return anyfloat.AnyFloat.from_float(res)

    def _anyfloat_calculator(self):
        calc = calculator.Calculator(float(self.first_num), float(self.second_num), self.operation)
        res = calc.calculate()
        return anyfloat.AnyFloat.from_float(res)

    def _hex_calculator(self):
        lhs = anyfloat.AnyFloat.from_ieee(int(self.first_num, 16))
        rhs = anyfloat.AnyFloat.from_ieee(int(self.second_num, 16))
        calc = calculator.Calculator(float(lhs), float(rhs), self.operation)
        res = calc.calculate()
        return anyfloat.AnyFloat.from_float(res)
