from cli import create_parser
from mode_1_input import read_data


def main():
    args = create_parser().parse_args()
    print(args)

    if args.m1:
        if not args.fin:
            raise IOError("Input file not specified")
        start_zone = read_data(args.fin)
        print("Max number of fields:", start_zone.solve())

    elif args.m2:
        pass

    elif args.m3:
        pass


if __name__ == "__main__":
    main()
