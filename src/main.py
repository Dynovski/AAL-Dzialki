from cli import create_parser


def main():
    args = create_parser().parse_args()
    print(args)

    if args.m1:
        pass

    if args.m2:
        pass

    if args.m3:
        pass


if __name__ == "__main__":
    main()
