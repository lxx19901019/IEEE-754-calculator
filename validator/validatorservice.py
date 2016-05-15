import re

OPERATIONS = ('+', '*', '/')
BIN32_FORMAT = 1
BIN64_FORMAT = 2
FLOAT_REPR = 1
HEX_REPR = 2
ROUND_MODES = (0, 1, 2, 3, 4)


class ValidatorService:
    @staticmethod
    def is_format_valid(format_or_repr):
        return _is_int(format_or_repr) and (int(format_or_repr) == BIN32_FORMAT or int(format_or_repr) == BIN64_FORMAT)

    @staticmethod
    def is_repr_valid(format_or_repr):
        return _is_int(format_or_repr) and \
            (int(format_or_repr) == FLOAT_REPR or int(format_or_repr) == HEX_REPR)

    @staticmethod
    def is_round_mode_valid(round_mode):
        return _is_int(round_mode) and int(round_mode) in ROUND_MODES

    @staticmethod
    def is_operator_valid(op):
        return op in OPERATIONS

    @staticmethod
    def is_hex_number_bin32_valid(hex_num):
        return len(hex_num) == 8 and re.match('[0-9a-fA-F]+', hex_num)

    @staticmethod
    def is_hex_number_bin64_valid(hex_num):
        return len(hex_num) == 16 and re.match('[0-9a-fA-F]+', hex_num)

    @staticmethod
    def is_float_number_valid(float_num):
        try:
            float(float_num)
            return True
        except ValueError:
            return False


def _is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
