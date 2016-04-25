import re

LEN_BIN32 = 32
LEN_BIN64 = 64
MAX_EXP32_VALUE = 255
MAX_SHORT_EXP32_VALUE = 127
MIN_SHORT_EXP32_VALUE = -128
MAX_SIGNIFICAND32_VALUE = 8388607
MAX_EXP64_VALUE = 2047
OPERATIONS = ('+', '*', '/')
SINGLE_PRECISION = 1
DOUBLE_PRECISION = 2
BIN32_FORMAT = 1
BIN64_FORMAT = 2
BIN_REPR = 1
ANYFLOAT_REPR = 2
HEX_REPR = 3


class ValidatorService:
    @staticmethod
    def is_format_valid(format_or_repr):
        return _is_int(format_or_repr) and (int(format_or_repr) == BIN32_FORMAT or int(format_or_repr) == BIN64_FORMAT)

    @staticmethod
    def is_repr_valid(format_or_repr):
        return _is_int(format_or_repr) and \
            (int(format_or_repr) == BIN_REPR or int(format_or_repr) == ANYFLOAT_REPR or int(format_or_repr) == HEX_REPR)

    @staticmethod
    def is_bin32_num_valid(bin32_num):
        return len(bin32_num) == LEN_BIN32 and bin32_num.count('1') + bin32_num.count('0') == LEN_BIN32

    @staticmethod
    def is_bin64_num_valid(bin64_num):
        return len(bin64_num) == LEN_BIN64 and bin64_num.count('1') + bin64_num.count('0') == LEN_BIN64

    @staticmethod
    def is_sign_num_valid(sign):
        return int(sign) == 1 or int(sign) == 0

    @staticmethod
    def is_exp32_num_valid(exp32_num):
        return _is_int(exp32_num) and \
               (int(exp32_num) >= 0 and int(exp32_num) <= MAX_EXP32_VALUE or
                int(exp32_num) >= MIN_SHORT_EXP32_VALUE and int(exp32_num) <= MAX_SHORT_EXP32_VALUE)

    @staticmethod
    def is_signif32_num_valid(signif32_num):
        return _is_int(signif32_num) and int(signif32_num) >= 0 and int(signif32_num) <= MAX_SIGNIFICAND32_VALUE

    @staticmethod
    def is_exp64_num_valid(exp64_num):
        return _is_int(exp64_num) and int(exp64_num) >= 0 and int(exp64_num) <= MAX_EXP64_VALUE

    @staticmethod
    def is_signif64_num_valid(signif64_num):
        return _is_int(signif64_num) and int(signif64_num) >= 0

    @staticmethod
    def is_operator_valid(op):
        return op in OPERATIONS

    @staticmethod
    def is_precision_valid(prec):
        return _is_int(prec) and (int(prec) == SINGLE_PRECISION or int(prec) == DOUBLE_PRECISION)

    @staticmethod
    def is_hex_number_bin32_valid(hex_num):
        return len(hex_num) == 8 and re.match('[0-9a-fA-F]+', hex_num)

    @staticmethod
    def is_hex_number_bin64_valid(hex_num):
        return len(hex_num) == 16 and re.match('[0-9a-fA-F]+', hex_num)

def _is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
