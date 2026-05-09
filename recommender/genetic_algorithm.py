import random

from recommender.models import (
    Product,
    Rating,
    Behavior
)

class GeneticRecommender:
    
    def __init__(self, user):
        self.user = user
    
    def create_population(self, population_size=10, recommendation_size=5):

        all_products = list(Product.objects.all())

        population = []

        for _ in range(population_size):

            chromosome = random.sample(
                all_products,
                recommendation_size
            )

            population.append(chromosome)

        return population


    def fitness(self, chromosome):

        score = 0

        for product in chromosome:

            behaviors = Behavior.objects.filter(
                user=self.user,
                product=product
            )

            ratings = Rating.objects.filter(
                user=self.user,
                product=product
            )

            for behavior in behaviors:

                if behavior.viewed:
                    score += 1

                if behavior.clicked:
                    score += 2

                if behavior.purchased:
                    score += 5

            for rating in ratings:
                score += rating.rating

        return score
    
    def selection(self, population):

        population = sorted(
            population,
            key=self.fitness,
            reverse=True
        )

        return population[:5]
    
    def crossover(self, parent1, parent2):

        split = len(parent1) // 2

        child = parent1[:split] + parent2[split:]

        return child
    
    def mutation(self, chromosome):

        all_products = list(Product.objects.all())

        random_index = random.randint(
            0,
            len(chromosome) - 1
        )

        chromosome[random_index] = random.choice(all_products)

        return chromosome
    
    def evolve(self, generations=20):

        population = self.create_population()

        for _ in range(generations):

            selected = self.selection(population)

            new_population = []

            while len(new_population) < 10:

                parent1 = random.choice(selected)
                parent2 = random.choice(selected)

                child = self.crossover(parent1, parent2)

                child = self.mutation(child)

                new_population.append(child)

            population = new_population

        best_solution = max(
            population,
            key=self.fitness
        )

        return best_solution