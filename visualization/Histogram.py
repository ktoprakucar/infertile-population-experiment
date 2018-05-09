import matplotlib.pyplot as plt


class Histogram:
    def show(self, populationList, populationSize, infertileSize, yearsToLive, maxAge):
        plt.title(
            "populationSize: {}, infertileSize: {}, yearsToLive: {}, maxAge: {}".format(populationSize, infertileSize,
                                                                                        yearsToLive, maxAge))
        plt.barh(list(populationList.keys()), populationList.values())
        # plt.bar(list(populationList.keys()), populationList.values(), color='g')
        plt.xlabel("Population")
        plt.ylabel("Year")
        plt.savefig(
            "/Users/toprak.ucar/Desktop/yLisans/introductionToBioinformatics/infertile-population-experiment/results/populationSize:{}-infertileSize:{}-yearsToLive:{}-maxAge:{}(childrenCanBeInfertile).png".format(
                populationSize, infertileSize, yearsToLive, maxAge))
        print(populationList)
        # plt.show()
