import random

from entity.Person import Person


class Breeding:
    def breed(self, population):
        if len(list(filter(lambda p: p.isBreed == False, population))) > 1:
            firstPerson = self.retrieveFirstPerson(population)
            secondPerson = self.retrieveSecondPerson(population, firstPerson.id)

            if (not (firstPerson.isInfertile or secondPerson.isInfertile) and (firstPerson.age == secondPerson.age)):
                child = Person(len(population), 0, False, True)
                #child = Person(len(population), 0, bool(random.getrandbits(1)), False)
                population.append(child)
                firstPerson.isBreed = True
                firstPerson.age = firstPerson.age + 1
                secondPerson.isBreed = True
                secondPerson.age = secondPerson.age + 1
            return True
        else:
            return False

    def retrieveFirstPerson(self, population):
        return random.choice([p for p in population if not p.isBreed])

    def retrieveSecondPerson(self, population, firstPersonId):
        return random.choice([p for p in population if (not p.isBreed) and (p.id != firstPersonId)])
