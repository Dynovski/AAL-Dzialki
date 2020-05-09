import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="Program oblicza maksymalną liczbę działek dla "
                                                 "pewnego obszaru R.")
    # Zmienne m1, m2, m3 przechowują informację czy zostały użyte w poleceniu
    parser.add_argument("-m1", action="store_true", help="Wczytaj dane z jednego pliku i wyprowadź wynik do innego. "
                                                         "Wymaga: in, out.")
    parser.add_argument("-m2", action="store_true", help="Wygeneruj i rozwiąż instancję problemu. Wymaga: ht, w ,n.")
    parser.add_argument("-m3", action="store_true", help="Przeprowadź proces testowania z pomiarem czasu dla "
                                                         "rosnącego problemu i porównanaj ze złożonością teoretyczną."
                                                         " Wymaga: ht, w, n, s, k, r.")
    # Flagi tla trybu 1
    parser.add_argument("-fin", help="nazwa pliku, z którego wczytywane zostaną dane")
    parser.add_argument("-fout", help="nazwa pliku, do którego zapisywany zostanie wynik", default="output.txt")

    # Flagi dla trybu 2
    parser.add_argument("-ht", help="wysokość obszaru R", type=int)
    parser.add_argument("-w", help="szerokość obszaru R", type=int)
    parser.add_argument("-n", help="liczba punktów do wygenerowania", type=int)

    # Flagi dla trybu 3
    parser.add_argument("-s", help="wartość, o jaką rosną początkowe wielkości co iterację", type=int)
    parser.add_argument("-k", help="liczba iteracji", type=int)
    parser.add_argument("-r", help="liczba powtórzeń na iterację", type=int)

    return parser
