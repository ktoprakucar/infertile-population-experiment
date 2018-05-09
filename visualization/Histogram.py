import matplotlib.pyplot as plt

class Histogram:

    def show(self, populationList, populationSize, infertileSize, yearToLive, maxAge):
        plt.bar(list(populationList.keys()), populationList.values(), color='g')
        plt.title("Population Histogram, populationSize: {}, infertileSize: {}, yearToLive: {}, maxAge: {}".format(populationSize, infertileSize, yearToLive, maxAge))
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.show()
