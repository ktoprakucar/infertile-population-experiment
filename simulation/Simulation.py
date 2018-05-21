from entity.Environment import Environment
from operation.Breeding import Breeding
from operation.Life import Life
from visualization.Histogram import Histogram


class Simulation:
    def simulate(self, populationSize, infertileSize, maxAge, yearsToLive):
        environment = Environment()
        breeding = Breeding()
        life = Life()
        histogram = Histogram()

        populationList = {}
        population = environment.generatePopulation(populationSize, infertileSize)

        for year in range(yearsToLive):
            for x in range(len(population)):
                isActive = breeding.breed(population)
                if not isActive:
                    break
            life.refreshAndGrow(population)
            population = life.die(population, maxAge)
            populationList[year] = len(population)
        histogram.show(populationList, populationSize, infertileSize, yearsToLive, maxAge)
