from validator import validatorservice
from floatprocesser import anyfloat


class ConsoleService:
    @staticmethod
    def print_message(msg):
        print(msg)

    @staticmethod
    def ask_message(msg):
        s = input(msg)
        if s != 'exit':
            return s
        else:
            raise RuntimeError

    @staticmethod
    def ask_format_or_repr(msg):
        while (True):
            s = ConsoleService.ask_message(msg)
            if int(s) == 1 or int(s) == 2:
                return int(s)

    @staticmethod
    def ask_bin32_num_in_bin_repr(msg):
        while (True):
            bin32_num = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_bin32_num_valid(bin32_num):
                return bin32_num
            else:
                ConsoleService.print_message('Invalid binary representation of bin32 num!')

    @staticmethod
    def ask_bin64_num_in_bin_repr(msg):
        while (True):
            bin64_num = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_bin64_num_valid(bin64_num):
                return bin64_num
            else:
                ConsoleService.print_message('Invalid binary representation of bin64 num!')

    @staticmethod
    def ask_sign_num(msg):
        while (True):
            sign = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_sign_num_valid(sign):
                return int(sign)
            else:
                ConsoleService.print_message('Invalid sign num!')

    @staticmethod
    def ask_anyfloat32_num(sign_msg, exp32_num_msg, signif32_num_msg):
        sign = ConsoleService.ask_sign_num(sign_msg)
        exp32_num = ConsoleService._ask_exp32_num(exp32_num_msg)
        signif32_num = ConsoleService._ask_signif32_num(signif32_num_msg)
        anyfloat32_num = anyfloat.AnyFloat(sign, exp32_num, signif32_num)
        return anyfloat32_num

    @staticmethod
    def _ask_exp32_num(msg):
        while (True):
            exp32_num = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_exp32_num_valid(exp32_num):
                return int(exp32_num)
            else:
                ConsoleService.print_message('Invalid exp32 num!')

    @staticmethod
    def _ask_signif32_num(msg):
        while (True):
            signif32_num = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_signif32_num_valid(signif32_num):
                return int(signif32_num)
            else:
                ConsoleService.print_message('Invalid signif32 num!')

    @staticmethod
    def ask_anyfloat64_num(sign_msg, exp64_num_msg, signif64_num_msg):
        sign = ConsoleService.ask_sign_num(sign_msg)
        exp64_num = ConsoleService._ask_exp64_num(exp64_num_msg)
        signif64_num = ConsoleService._ask_signif64_num(signif64_num_msg)
        anyfloat64_num = anyfloat.AnyFloat(sign, exp64_num, signif64_num)
        return anyfloat64_num

    @staticmethod
    def _ask_exp64_num(msg):
        while (True):
            exp64_num = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_exp64_num_valid(exp64_num):
                return int(exp64_num)
            else:
                ConsoleService.print_message('Invalid exp64 num!')

    @staticmethod
    def _ask_signif64_num(msg):
        while (True):
            signif64_num = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_signif64_num_valid(signif64_num):
                return int(signif64_num)
            else:
                ConsoleService.print_message('Invalid signif64 num!')

    @staticmethod
    def ask_operator(msg):
        while (True):
            operator = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_operator_valid(operator):
                return operator
            else:
                ConsoleService.print_message('Invalid operator!')
