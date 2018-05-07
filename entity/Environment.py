from entity.Person import Person

class Environment:

    def generatePopulation(self, size, infertilePersonAmount):
        population = []
        for x in range(size):
            if(infertilePersonAmount > 0):
                population.append(Person(x, True, False))
                infertilePersonAmount = infertilePersonAmount - 1
            else:
                population.append(Person(x, False, False))
        return population


