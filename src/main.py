from cli import create_parser
import mode_1
import mode_2
import mode_3
import plotting


def main():
    args = create_parser().parse_args()

    if args.m1:
        if not args.fin:
            raise IOError("Input file not specified")
        start_zone = mode_1.read_data(args.fin)
        max_num, trace = start_zone.solve()
        mode_1.store_answer(args.fout, (max_num, trace))
        plotting.draw_problem(start_zone, trace)

    elif args.m2:
        start_zone = mode_2.generate_instance(args.w, args.ht, args.n)
        max_num, trace = start_zone.solve()
        mode_2.store_answer(start_zone, (max_num, trace))
        plotting.draw_problem(start_zone, trace)

    elif args.m3:
        mode_3.start_testing(args.w, args.ht, args.n, args.s, args.k, args.r)


if __name__ == "__main__":
    main()
