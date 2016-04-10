class ConsoleService:
    @staticmethod
    def print_message(msg):
        print(msg)

    @staticmethod
    def ask_format_or_repr(msg):
        while (True):
            s = input(msg)
            if int(s) == 1 or int(s) == 2:
                return int(s)

    @staticmethod
    def ask_num(msg):
        while (True):
            num = input(msg)
            return num

    @staticmethod
    def ask_operation(msg):
        while (True):
            op = input(msg)
            return op
