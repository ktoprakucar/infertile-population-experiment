from simulation.Simulation import Simulation


class Application:
    simulation = Simulation()
    maxAge = 5
    populationSize = 100
    infertileSize = 0
    yearToLive = 25

    for x in range(8):
        print("PopulationSize: {}, infertileSize: {}, yearToLive: {}, maxAge: {}".format(populationSize, infertileSize,
                                                                                         yearToLive, maxAge))
        simulation.simulate(populationSize, infertileSize, maxAge, yearToLive)
        infertileSize = infertileSize + 10
