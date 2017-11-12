import numpy as np
import genetics
import intervals as intervalo

OBS_1X = intervalo.FloatInterval.closed(0.75, 1.25)
OBS_1Y = intervalo.FloatInterval.closed(0.75, 1.25)

OBS_2X = intervalo.FloatInterval.closed(1.25, 1.75)
OBS_2Y = intervalo.FloatInterval(3.25, 3.75)

OBS_3X = intervalo.FloatInterval.closed(2.25, 2.75)
OBS_3Y = intervalo.FloatInterval.closed(2.25, 2.75)

OBS_4X = intervalo.FloatInterval.closed(4.25, 4.75)
OBS_4Y = intervalo.FloatInterval.closed(1.75, 2.25)

OBS_5X = intervalo.FloatInterval.closed(2.75, 3.25)
OBS_5Y = intervalo.FloatInterval.closed(0.75, 1.25)

OBS_6X = intervalo.FloatInterval.closed(3.75, 4.25)
OBS_6Y = intervalo.FloatInterval.closed(2.75, 3.25)

populacao = genetics.generatePopulation(1,2)

# print populacao[0]
#
# print populacao[0][0]-populacao[0][1]
#
# dist = np.linalg.norm(populacao[0][0]-populacao[0][1])
#
# print dist