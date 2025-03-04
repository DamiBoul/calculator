import argparse
from calculator import Calculator

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-op", "--operation", help="(sum, ...)")
    parser.add_argument("-val1", "--first_value", type=int, help="Give the firt value")
    parser.add_argument("-val2", "--second_value", type=int, help="Give the second value")
    parser.add_argument("-val3", "--second_value", type=int, help="Give the third value", nargs='?', default=None)

    args = parser.parse_args()
    calc = Calculator()

    if args.operation == 'sum':
        print(f'{args.first_value} + {args.second_value} = {calc.mysum(args.first_value, args.second_value)}')
    elif args.operation == 'max':
        print(f'The max between {args.first_value}, {args.second_value}, {args.third_value} is {calc.mymax(args.first_value, args.second_value, args.third_value)}')
    else :
        print('The function is not taken into account in our calculator')