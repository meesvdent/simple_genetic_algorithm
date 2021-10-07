# Testing Chromosome class methods

from simple_genetic_algorithm import Chromosome


def test_chromosome():
    father = Chromosome([0, 1, 1, 2, 3, 4, 5])
    mother = Chromosome([10, 39, 59, 72, 59, 10, 99])

    print(father)
    print(mother)

    print(father.crossover(mother))


def main():
    test_chromosome()


if __name__ == "__main__":
    main()
