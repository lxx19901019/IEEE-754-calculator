from consolehelper import consoleservice
from ioprocessers import inputdataprocesser
from ioprocessers import outputdataprocesser
from validator import validatorservice
import argparse


def main():
    try:
        parser = argparse.ArgumentParser(description='console ieee-754 calculator')
        parser.add_argument('-f', '--format', type=int,
                            help='(1)bin32 or (2)bin64')
        parser.add_argument('-r', '--representation', type=int,
                            help='(1)float or (2)hex(without "0x" prefix)')
        parser.add_argument('-rm', '--roundmode', type=int,
                            help='(0)nearest even (1)to 0 (2)to -inf (3)to +inf (4)nearest odd')
        parser.add_argument('-num1', '--firstnum', type=str,
                            help='first num in chosen format & representation')
        parser.add_argument('-num2', '--secondnum', type=str,
                            help='second num in chosen format & representation')
        parser.add_argument('-op', '--operation', type=str,
                            help='arithmetic operation(+,*,/)')

        args = parser.parse_args()

        validate_input(args) #raises RuntimeError when input data is not valid

        in_proc = inputdataprocesser.InputProcesser(args.format, args.representation, args.roundmode, args.firstnum,
                                                    args.secondnum, args.operation)
        res_and_excode = in_proc.process()
        out_proc = outputdataprocesser.OutputProcesser(res_and_excode[0], res_and_excode[1], args.format)
        out_proc.process()
    except RuntimeError:
        consoleservice.ConsoleService.print_message('For more info - use --help')
        consoleservice.ConsoleService.print_message('Bye!')


def validate_input(args):
        if not validatorservice.ValidatorService.is_format_valid(args.format):
            consoleservice.ConsoleService.print_message('Invalid format! Choose - 1 for bin32 or 2 - for bin64!')
            raise RuntimeError()

        if not validatorservice.ValidatorService.is_repr_valid(args.representation):
            consoleservice.ConsoleService.print_message('Invalid representation! Choose - 1 for float or 2 - for hex!')
            raise RuntimeError()

        if not validatorservice.ValidatorService.is_round_mode_valid(args.roundmode):
            consoleservice.ConsoleService.print_message('Invalid round mode!')
            raise RuntimeError()

        if not validatorservice.ValidatorService.is_operator_valid(args.operation):
            consoleservice.ConsoleService.print_message('Invalid operation! Valid operations: +, *, /')
            raise RuntimeError()

        if args.format == 1 and args.representation == 2:
            if not validatorservice.ValidatorService.is_hex_number_bin32_valid(args.firstnum):
                consoleservice.ConsoleService.print_message('Invalid first num!')
                raise RuntimeError()
            if not validatorservice.ValidatorService.is_hex_number_bin32_valid(args.secondnum):
                consoleservice.ConsoleService.print_message('Invalid second num!')
                raise RuntimeError()

        if args.format == 2 and args.representation == 2:
            if not validatorservice.ValidatorService.is_hex_number_bin64_valid(args.firstnum):
                consoleservice.ConsoleService.print_message('Invalid first num!')
                raise RuntimeError()
            if not validatorservice.ValidatorService.is_hex_number_bin64_valid(args.secondnum):
                consoleservice.ConsoleService.print_message('Invalid second num!')
                raise RuntimeError()

        if (args.format == 1 or args.format == 2) and args.representation == 1:
            if not validatorservice.ValidatorService.is_float_number_valid(args.firstnum):
                consoleservice.ConsoleService.print_message('Invalid first num!')
                raise RuntimeError()
            if not validatorservice.ValidatorService.is_float_number_valid(args.secondnum):
                consoleservice.ConsoleService.print_message('Invalid second num!')
                raise RuntimeError()


if __name__ == '__main__':
    main()
