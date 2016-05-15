from consolehelper import consoleservice
from ioprocessers import inputdataprocesser
from ioprocessers import outputdataprocesser

CHOOSE_FORMAT = 'Choose a format of numbers for calculation: (1)binary32 or (2)binary64:'
CHOOSE_REPR = 'Choose a representation of numbers: (1)Float or (2)Hex(without "0x" prefix):'
CHOOSE_ROUND_MODE = 'Choose a round mode: (0)to nearest even (1)to 0 (2)to -infinity (3)to +infinity (4)to nearest odd:'

"""
How to read exception mask:

For example: 0b101

Read it from the right to left(<-)
Answer: inexact & overflow exception

bit 0   inexact exception
bit 1	underflow exception
bit 2	overflow exception
bit 3	infinite exception (“divide by zero”)
bit 4	invalid exception
"""


def main():
    try:
        number_format = consoleservice.ConsoleService.ask_format(CHOOSE_FORMAT)
        number_repr = consoleservice.ConsoleService.ask_repr(CHOOSE_REPR)
        round_mode = consoleservice.ConsoleService.ask_round(CHOOSE_ROUND_MODE)
        in_proc = inputdataprocesser.InputProcesser(number_format, number_repr, round_mode)
        res_and_excode = in_proc.process()
        out_proc = outputdataprocesser.OutputProcesser(res_and_excode[0], res_and_excode[1], number_format)
        out_proc.process()
    except RuntimeError:
        consoleservice.ConsoleService.print_message('\nBye!')

if __name__ == '__main__':
    main()
