# Simple Genetic Algorithm as described by Goldberg

import random
import numpy as np

class Chromosome():

    def __init__(self, sequence):
        self.sequence = np.array(sequence)

    def crossover(self, other):
        point = random.randrange(0, len(self.sequence))
        self_parent = self.sequence[0:point]
        other_parent = other.sequence[point : len(other.sequence) ]
        child = np.concatenate((self_parent, other_parent))
        return child


