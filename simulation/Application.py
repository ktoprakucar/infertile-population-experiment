from entity.Environment import Environment

class Application:

    environment = Environment()
    population = environment.generatePopulation(100, 30)
    print("bla bla bla")
