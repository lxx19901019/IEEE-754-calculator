from validator import validatorservice


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
    def ask_format(msg):
        while (True):
            s = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_format_valid(s):
                return int(s)
            else:
                ConsoleService.print_message('Invalid format num!')

    @staticmethod
    def ask_repr(msg):
        while (True):
            s = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_repr_valid(s):
                return int(s)
            else:
                ConsoleService.print_message('Invalid representation num!')

    @staticmethod
    def ask_operator(msg):
        while (True):
            operator = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_operator_valid(operator):
                return operator
            else:
                ConsoleService.print_message('Invalid operator!')

    @staticmethod
    def ask_round(msg):
        while (True):
            r = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_round_mode_valid(r):
                return int(r)
            else:
                ConsoleService.print_message('Invalid round mode!')

    @staticmethod
    def ask_hex32_num(msg):
        while (True):
            hex32_num = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_hex_number_bin32_valid(hex32_num):
                return hex32_num
            else:
                ConsoleService.print_message('Invalid hex32 num!')

    @staticmethod
    def ask_hex64_num(msg):
        while (True):
            hex64_num = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_hex_number_bin64_valid(hex64_num):
                return hex64_num
            else:
                ConsoleService.print_message('Invalid hex64 num!')

    @staticmethod
    def ask_float_num(msg):
        while (True):
            float_num = ConsoleService.ask_message(msg)
            if validatorservice.ValidatorService.is_float_number_valid(float_num):
                return float(float_num)
            else:
                ConsoleService.print_message('Invalid float num!')
