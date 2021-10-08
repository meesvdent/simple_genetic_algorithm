# Simple Genetic Algorithm as described by Goldberg

import random
import numpy as np
from helpers import flip_boolean

class Chromosome():

    def __init__(self, sequence, pm):
        self.sequence = np.array(sequence)
        self.pm = pm

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

