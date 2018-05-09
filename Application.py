from simulation.Simulation import Simulation


class Application:
    simulation = Simulation()
    maxAge = 5
    populationSize = 100
    infertileSize = 0
    yearsToLive = 5

    for x in range(8):
        print("PopulationSize: {}, infertileSize: {}, yearToLive: {}, maxAge: {}".format(populationSize, infertileSize,
                                                                                         yearsToLive, maxAge))
        simulation.simulate(populationSize, infertileSize, maxAge, yearsToLive)
        infertileSize = infertileSize + 10
