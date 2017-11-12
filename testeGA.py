import genetics

gene = genetics.generateGene()

cromossomo = genetics.generateChromosome(6)

populacao = genetics.generatePopulation(20,4)

for i in range(len(populacao)):
    print populacao[i]