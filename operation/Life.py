class Life:
    def die(self, population, maxAge):
        return list(filter(lambda p: p.age < maxAge, population))

    def refreshAndGrow(self, population):
        for p in population:
            p.isBreed = False
            p.age = p.age + 1
