from utilities.cli import create_parser
from modes import mode_1, mode_2, mode_3
from utilities import graphic_solution


def main():
    args = create_parser().parse_args()

    if args.m1:
        if not args.fin:
            raise IOError("Input file not specified")
        start_zone = mode_1.read_data(args.fin)
        max_num_of_fields, points_of_intersection = start_zone.solve()
        mode_1.store_answer(args.fout, (max_num_of_fields, points_of_intersection))
        graphic_solution.draw(start_zone, points_of_intersection)

    elif args.m2:
        start_zone = mode_2.generate_instance(args.w, args.ht, args.n)
        max_num_of_fields, points_of_intersection = start_zone.solve()
        mode_2.store_answer(start_zone, (max_num_of_fields, points_of_intersection))
        graphic_solution.draw(start_zone, points_of_intersection)

    elif args.m3:
        mode_3.benchmark(args.w, args.ht, args.n, args.s, args.k, args.r)


if __name__ == "__main__":
    main()
