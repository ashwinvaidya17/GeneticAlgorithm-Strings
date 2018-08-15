from population import Population
from dna import DNA
import math

target = "To be or not to be."
popmax = 200
mutationRate = 0.01

population = Population(target, mutationRate, popmax)

def displayInfo():
	answer = population.getBest()

	statsText = "Total generations   " + str(population.getGenerations()) + "\n"
	statsText += "Average Fitness   " + str(population.getAverageFitness()) + "\n"
	statsText += "Total Population   " + str(popmax) + "\n"
	statsText += "Mutation Rate   " + str(mutationRate *100) + "%\n"
	print("All Phrases: " + population.allPhrases())
	print(statsText)
	print(answer + "\n")

while True:
	
	population.naturalSelection()

	population.generate()

	population.calcFitness()

	population.evaluate()

	displayInfo()

	if population.isFinished():
		break



