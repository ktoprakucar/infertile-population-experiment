class Life:
    def die(self, population, maxAge):
        return list(filter(lambda p: p.age < maxAge, population))

    def refresh(self, population):
        for p in population:
            p.isBreed = False
