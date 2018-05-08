from entity.Environment import Environment
from operation.Breeding import Breeding
from operation.Life import Life


class Application:
    maxAge = 3
    environment = Environment()
    breeding = Breeding()
    life = Life()
    populationList = []

    population = environment.generatePopulation(50, 30)
    for year in range(10):
        for x in range(len(population)):
            isActive = breeding.breed(population)
            print(len(population))
            if not isActive:
                break
        population = life.die(population, maxAge)
        life.refresh(population)
        populationList.append(len(population))
        print("year: {}".format(year))
    print(populationList)

