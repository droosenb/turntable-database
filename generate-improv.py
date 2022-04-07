import numpy as np


def generateExercise(adj, techniques, numAdj, numTechniques):
    line = ""
    for i in range(numAdj):
        line += np.random.choice(adj)
    for j in range(numTechniques):
        line += np.random.choice(techniques)
    return line


def openDatabase(numAdj, numTechniques, numEx):
    adjectivesF = open("database/adj.txt", "r")
    techniquesF = open("database/techniques.txt", "r")

    adjectives = adjectivesF.readlines()
    techniques = techniquesF.readlines()

    print("\n")
    print("\n")

    for i in range(numEx):
        print(generateExercise(adjectives, techniques, numAdj, numTechniques))
        print("\n")

    print("\n")
    print("\n")


if __name__ == "__main__":
    openDatabase(1, 2, 3)
