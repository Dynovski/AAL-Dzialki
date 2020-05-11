from cli import create_parser
import mode_1
import mode_2


def main():
    args = create_parser().parse_args()
    print(args)

    if args.m1:
        if not args.fin:
            raise IOError("Input file not specified")
        start_zone = mode_1.read_data(args.fin)
        mode_1.store_answer(args.fout, start_zone.solve())

    elif args.m2:
        start_zone = mode_2.generate_instance(args.w, args.ht, args.n)
        mode_2.store_answer(start_zone, start_zone.solve())

    elif args.m3:
        pass


if __name__ == "__main__":
    main()
