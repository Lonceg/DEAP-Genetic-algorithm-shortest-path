from suppo import Environment
import random
import numpy as np
import math

from deap import base
from deap import creator
from deap import tools

g = 0
limit = 100
population = 20000
points = 3

creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

env = Environment()
env.readJson('scen3.json')

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.uniform, 0, 1)

toolbox.register("individual", tools.initRepeat, creator.Individual,
    toolbox.attr_bool, 2*points)

toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalOneMin(individual):

    i = 0
    total = 0
    current = np.array([env.start[0],env.start[1]])
    while i <= (points*2)-2:
        new = np.array([individual[i], individual[i + 1]])
        path = math.dist(current, new)
        total = total + path

        for x in env.staticObstacles:
            obstacle = np.array([x[0],x[1]])
            path_obstacle = math.dist(current, obstacle)
            if path_obstacle <= path:
                d = np.abs(np.linalg.norm(np.cross(new - current, obstacle - current))) / np.linalg.norm(new - current)
                if d < x[2]:
                    if g < 0.1*limit:
                        total = total + 10
                    elif g < 0.2*limit:
                        total = total + 10
                    else:
                        total = total + 10

        if current[0] < 0 or current[1] < 0 or current[0] > 1 or current[1] > 1:
            total = total + 10

        current = new
        i = i + 2

    total = total + math.dist(current, env.stop)
    new = np.array([env.stop[0], env.stop[1]])
    path = math.dist(current, new)

    for x in env.staticObstacles:
        obstacle = np.array([x[0], x[1]])
        path_obstacle = math.dist(current, obstacle)
        if path_obstacle <= path:
            d = np.abs(np.linalg.norm(np.cross(new - current, obstacle - current))) / np.linalg.norm(new - current)
            if d < x[2]:
                if g < 0.1 * limit:
                    total = total + 10
                elif g < 0.2 * limit:
                    total = total + 10
                else:
                    total = total + 10

    return total,



toolbox.register("evaluate", evalOneMin)

toolbox.register("mate", tools.cxTwoPoint)

toolbox.register("mutate", tools.mutGaussian, mu=0.5, sigma=0.5, indpb=0.2)

toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(64)

    pop = toolbox.population(n=population)

    CXPB, MUTPB = 0.1, 0.6

    print("Start of evolution")

    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print("  Evaluated %i individuals" % len(pop))

    fits = [ind.fitness.values[0] for ind in pop]

    g=0
    while g < limit:
        g = g + 1
        print("-- Generation %i --" % g)

        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):

            if random.random() < CXPB:
                toolbox.mate(child1, child2)

                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:

            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        print("  Evaluated %i individuals" % len(invalid_ind))

        pop[:] = offspring

        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5
        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)

    print("-- End of (successful) evolution --")
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))

    env.plot(points, best_ind)

if __name__ == "__main__":
    main()