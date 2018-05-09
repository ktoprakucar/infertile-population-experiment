from simulation.Simulation import Simulation


class Application:
    simulation = Simulation()
    maxAge = 3
    populationSize = 100
    infertileSize = 30
    yearToLive = 7
    print("PopulationSize: {}, infertileSize: {}, yearToLive: {}, maxAge: {}".format(populationSize, infertileSize, yearToLive, maxAge))
    simulation.simulate(populationSize, infertileSize, maxAge, yearToLive)
