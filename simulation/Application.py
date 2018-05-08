from entity.Environment import Environment
from operation.Breeding import Breeding


class Application:
    environment = Environment()
    breeding = Breeding()
    population = environment.generatePopulation(100, 30)
    for x in range(50):
        breeding.breed(population)
        print(len(population))
