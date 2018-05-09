import random

from entity.Person import Person


class Breeding:
    def breed(self, population):
        if len(list(filter(lambda p: p.isBreed == False, population))) > 1:
            firstPerson = self.retrieveFirstPerson(population)

            secondPerson = self.retrieveSecondPerson(population, firstPerson.id)
            # print("firstPerson id: {} isInfertile: {}".format(firstPerson.id, firstPerson.isInfertile))
            # print("secondPerson id: {} isInfertile: {}".format(secondPerson.id, secondPerson.isInfertile))

            if (not (firstPerson.isInfertile or secondPerson.isInfertile) and (firstPerson.age == secondPerson.age)):
                child = Person(len(population), 0, False, True)
                # child = Person(len(population), 0, bool(random.getrandbits(1)), False)
                population.append(child)
                firstPerson.isBreed = True
                firstPerson.age = firstPerson.age + 1
                secondPerson.isBreed = True
                secondPerson.age = secondPerson.age + 1
                # print("child was born id: {}".format(child.id))
            return True
        else:
            print("End of year")
            return False

    def retrieveFirstPerson(self, population):
        return random.choice([p for p in population if not p.isBreed])

    def retrieveSecondPerson(self, population, firstPersonId):
        return random.choice([p for p in population if (not p.isBreed) and (p.id != firstPersonId)])
