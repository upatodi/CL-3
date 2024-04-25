import random
from deap import creator, base, tools, algorithms

# Create a maximization fitness class
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# Create an individual class representing a list of binary values
creator.create("Individual", list, fitness=creator.FitnessMax)

# Create a toolbox to register functions
toolbox = base.Toolbox()

# Register a function to generate a random binary attribute
toolbox.register("attr_bool", random.randint, 0, 1)
# Register a function to create an individual with 'n' binary attributes
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=100)
# Register a function to create a population of individuals
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Define the evaluation function to evaluate the fitness of an individual
def evalOneMax(individual):
    return sum(individual),

toolbox.register("evaluate", evalOneMax)
# Register genetic operators: crossover, mutation, and selection
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Create an initial population of individuals
population = toolbox.population(n=300)

# Define the number of generations
NGEN=40
# Evolution loop
for gen in range(NGEN):
    # Generate offspring by applying crossover and mutation to the population
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    # Evaluate the fitness of each offspring
    fits = toolbox.map(toolbox.evaluate, offspring)
    # Assign the fitness values to the offspring
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    # Select the next generation based on fitness
    population = toolbox.select(offspring, k=len(population))
# Select the top 10 individuals with the highest fitness
top10 = tools.selBest(population, k=10)
# Print the length of the first individual in the top 10 list
print(len(top10[0]))
