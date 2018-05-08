import random

from entity.Person import Person


class Breeding:

    def breed(self, population):
        firstPerson = self.retrieveFirstPerson(population)
        secondPerson = self.retrieveSecondPerson(population, firstPerson.id)
        print("firstPerson id: {} isInfertile: {}".format(firstPerson.id, firstPerson.isInfertile))
        print("secondPerson id: {} isInfertile: {}".format(secondPerson.id, secondPerson.isInfertile))

        if( not (firstPerson.isInfertile or secondPerson.isInfertile) ):
            population.append(Person(len(population), 0, False, False))

    def retrieveFirstPerson(self, population):
        return random.choice([p for p in population if not p.isBreed])

    def retrieveSecondPerson(self, population, firstPersonId):
        return random.choice([p for p in population if (not p.isBreed) and (p.id != firstPersonId)])