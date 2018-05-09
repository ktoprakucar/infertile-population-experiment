import matplotlib.pyplot as plt


class Histogram:
    def show(self, populationList, populationSize, infertileSize, yearToLive, maxAge):
        plt.title("populationSize: {}, infertileSize: {}, yearToLive: {}, maxAge: {}".format(populationSize, infertileSize,yearToLive, maxAge))
        plt.barh(list(populationList.keys()), populationList.values())
        #plt.bar(list(populationList.keys()), populationList.values(), color='g')
        plt.xlabel("Population")
        plt.ylabel("Year")
        plt.savefig(
            "/Users/toprak.ucar/Desktop/yLisans/introductionToBioinformatics/infertile-population-experiment/results/populationSize:{}-infertileSize:{}-yearToLive:{}-maxAge:{}.png".format(
                populationSize, infertileSize, yearToLive, maxAge))
        print(populationList)
        # plt.show()
