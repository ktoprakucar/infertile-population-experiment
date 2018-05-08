import matplotlib.pyplot as plt

class Histogram:

    def show(self, populationList):
        plt.bar(list(populationList.keys()), populationList.values(), color='g')
        plt.title("Population Histogram")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.show()
