from entity.Environment import Environment
from operation.Breeding import Breeding
from operation.Life import Life
from visualization.Histogram import Histogram

class Simulation:

    def simulate(self, populationSize, infertileSize, maxAge, yearToLive):
        environment = Environment()
        breeding = Breeding()
        life = Life()
        histogram = Histogram()

        populationList = {}
        population = environment.generatePopulation(populationSize, infertileSize)

        for year in range(yearToLive):
            for x in range(len(population)):
                isActive = breeding.breed(population)
                # print(len(population))
                if not isActive:
                    break
            population = life.die(population, maxAge)
            life.refresh(population)
            populationList[year] = len(population)
            print("year: {}".format(year))
        histogram.show(populationList, populationSize, infertileSize, yearToLive, maxAge)
