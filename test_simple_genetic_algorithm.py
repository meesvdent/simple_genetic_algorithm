# Testing Chromosome class methods

from simple_genetic_algorithm import Chromosome
import random
import numpy as np

def test_chromosome():
    father = Chromosome([False, False, False, False, False], pm = 0.2)
    mother = Chromosome([True, True, True, True, True], pm = 0.2)
    child = test_crossover(father, mother)
    print(child.sequence)

    child = test_mutate(child)
    print(child.sequence)


def test_mutate(chromosome):
    return chromosome.mutate()

def test_crossover(father, mother):
    return father.crossover(mother)

def main():
    test_chromosome()


if __name__ == "__main__":
    main()
