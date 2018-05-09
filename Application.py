from simulation.Simulation import Simulation


class Application:
    simulation = Simulation()

    maxAge = 3
    populationSize = 100
    infertileSize = 30
    yearToLive = 10

    simulation.simulate(populationSize, infertileSize, maxAge, yearToLive)
