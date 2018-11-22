import random


class GeneticAlgorithm:
    def __init__(self, locus_size, locus_num, population_num, probability_crossover, probability_mutation, crossover_num):
        self.locus_size = locus_size
        self.locus_num = locus_num
        self.population_num = population_num
        self.probability_crossover = probability_crossover
        self.probability_mutation = probability_mutation

        self.evaluation_method = None
        self.selection_method = []
        self.selection_num = []
        self.selection_option = []
        self.crossover_method = None
        self.crossover_num = crossover_num
        self.mutation_method = None

        self.population = []
        self.evaluation = []

    def proceed(self):
        self.evaluation = []
        for individual in self.population:
            self.evaluation.append(self.evaluate(individual))

        selected = self.select(self.evaluation)
        children = []
        while len(children) < self.crossover_num:
            parent = random.sample(selected, 2)
            children.extend(self.crossover(parent[0], parent[1]))

        self.mutation()

    def evaluate(self, individual):
        evaluation = self.evaluation_method(individual)
        return evaluation

    def generate_individual(self):
        individual = []
        for i in range(self.locus_size * self.locus_num):
            individual.append(random.randint(0, 1))
        return individual

    def generate_population(self):
        self.population = [self.generate_individual() for i in range(self.population_num)]

    def add_selection_method(self, method, option):
        self.selection_method.append(method)
        self.selection_option.append(option)

    def set_evaluation_method(self, method):
        self.evaluation_method = method

    def set_crossover_method(self, method):
        self.crossover_method = method

    def set_mutation_method(self, method):
        self.mutation_method = method

    def select(self, evaluation):
        result = list()
        for method, option in zip(self.selection_method, self.selection_option):
            result.extend(method(self.population, evaluation, option))
        return result

    def crossover(self, parent1, parent2):
        result = self.crossover_method(parent1, parent2)
        return result

    def mutation(self):
        if self.mutation_method is not None:
            self.mutation_method(self.population, self.probability_mutation)

