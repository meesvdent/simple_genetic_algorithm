# Testing Chromosome class methods

from simple_genetic_algorithm import Chromosome, Population
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

def test_population():
    chrom_one = Chromosome([False, False, True, True, False, False], pm = 0.2)
    chrom_two = Chromosome([False, False, True, True, False, False], pm = 0.2)
    chrom_three = Chromosome([False, False, True, True, False, False], pm = 0.2)
    chrom_four = Chromosome([False, False, True, True, False, False], pm = 0.2)
    chrom_five = Chromosome([False, False, True, True, False, False], pm = 0.2)
    chrom_array = np.array([chrom_one, chrom_two, chrom_three, chrom_four, chrom_five])
    population = Population(np.array(chrom_array), pm=0.1, pc=1.0, lambdaa=4)
    print(population.match_up(2))

    population.run(iterations=5)

def main():
    test_chromosome()
    test_population()

if __name__ == "__main__":
    main()
