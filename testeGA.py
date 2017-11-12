import numpy as np
import genetics


OBS_1X = np.linspace(0.75, 1.25, num=20)
OBS_1Y = np.linspace(0.75, 1.25, num=20)

OBS_2X = np.linspace(1.25, 1.75, num=20)
OBS_2Y = np.linspace(3.25, 3.75, num=20)

OBS_3X = np.linspace(2.25, 2.75, num=20)
OBS_3Y = np.linspace(2.25, 2.75, num=20)

OBS_4X = np.linspace(4.25, 4.75, num=20)
OBS_4Y = np.linspace(1.75, 2.25, num=20)

OBS_5X = np.linspace(2.75, 3.25, num=20)
OBS_5Y = np.linspace(0.75, 1.25, num=20)

OBS_6X = np.linspace(3.75, 4.25, num=20)
OBS_6Y = np.linspace(2.75, 3.25, num=20)

obstaculos = [[OBS_1X, OBS_1Y], [OBS_2X, OBS_2Y], [OBS_3X, OBS_3Y],
                       [OBS_4X, OBS_4Y], [OBS_5X, OBS_5Y], [OBS_6X, OBS_6Y]]


ponto = [1.2, 1.6]

print OBS_1Y
