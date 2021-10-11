# Simple Genetic Algorithm as described by Goldberg

import random
import numpy as np
from helpers import flip_boolean

class Chromosome():

    def __init__(self, sequence, pm):
        self.sequence = np.array(sequence)
        self.pm = pm

    def __str__(self):
        return str(self.sequence)

    def crossover(self, other):
        point = random.randrange(0, len(self.sequence))
        self_parent = self.sequence[0:point]
        other_parent = other.sequence[point : len(other.sequence)]
        child = np.concatenate((self_parent, other_parent))
        return Chromosome(child, self.pm)

    def mutate(self):
        # for every bit, change with chance pm
        mutated = [(random.random()<self.pm) for i in range(len(self.sequence))]
        self.sequence = flip_boolean(self.sequence, mutated)
        return self


class Population():

    def __init__(self, induviduals, pm, pc, lambdaa):
        self.individuals = np.array(induviduals)
        self.pm = pm
        self.pc = pc
        self.lambdaa = lambdaa
        self.children = []

    def __str__(self):
        string = ""
        for individual in self.individuals:
            string += (str(individual) + "\n")
        return string

    def match_up(self, k):
        matches = []
        random_order = random.sample(list(self.individuals), k=len(self.individuals))
        while len(random_order) > 2:
            matches.append((random_order[0], random_order[1]))
            random_order.pop(0)
            random_order.pop(0)
        return matches

    def crossover(self):
        matches = self.match_up(2)
        for match in matches:
            self.children.append(match[0].crossover(match[1]))

    def mutate_children(self):
        mutated = []
        for child in self.children:
            mutated.append(child.mutate())
        self.children = mutated

    def append_children(self):
        self.individuals = np.concatenate((self.individuals, self.children))

    def remove_children(self):
        self.children = []

    def select(self):
        remove = random.sample(range(len(self.individuals)), len(self.individuals) - self.lambdaa)
        self.individuals = np.delete(self.individuals, remove)

    def print_individuals(self):
        for individual in self.individuals:
            print(individual)

    def run(self, iterations=5):
        n = 0
        while n < iterations:
            self.crossover()
            self.mutate_children()
            self.append_children()
            self.remove_children()
            self.select()
            print("Iteration ", n+1)
            print(self)
            n += 1


