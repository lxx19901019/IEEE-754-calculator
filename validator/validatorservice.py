LEN_BIN32 = 32
LEN_BIN64 = 64
MAX_EXP32_VALUE = 255
MAX_SIGNIFICAND32_VALUE = 8388607
MAX_EXP64_VALUE = 2047
OPERATIONS = ('+', '-', '/')


class ValidatorService:
    @staticmethod
    def is_bin32_num_valid(bin32_num):
        if len(bin32_num) == 32 and bin32_num.count('1') + bin32_num.count('0') == LEN_BIN32:
            return True
        else:
            return False

    @staticmethod
    def is_bin64_num_valid(bin64_num):
        if len(bin64_num) == 64 and bin64_num.count('1') + bin64_num.count('0') == LEN_BIN64:
            return True
        else:
            return False

    @staticmethod
    def is_sign_num_valid(sign):
        if int(sign) == 1 or int(sign) == 0:
            return True
        else:
            return False

    @staticmethod
    def is_exp32_num_valid(exp32_num):
        if _is_int(exp32_num):
            if int(exp32_num) >= 0 and int(exp32_num) <= MAX_EXP32_VALUE:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def is_signif32_num_valid(signif32_num):
        if _is_int(signif32_num):
            if int(signif32_num) >= 0 and int(signif32_num) <= MAX_SIGNIFICAND32_VALUE:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def is_exp64_num_valid(exp64_num):
        if _is_int(exp64_num):
            if int(exp64_num) >= 0 and int(exp64_num) <= MAX_EXP64_VALUE:
                return True
            else:
                return False
        return False

    @staticmethod
    def is_signif64_num_valid(signif64_num):
        if _is_int(signif64_num):
            if signif64_num >= 0:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def is_operator_valid(op):
        if op in OPERATIONS:
            return True
        else:
            return False


def _is_int(num):
    try:
        int(num)
        return True
    except TypeError:
        return False
