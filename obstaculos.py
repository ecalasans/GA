import numpy as np
import scipy.spatial.distance as ssd

#obstaculo 1
x1 = np.linspace(0.75, 1.25, num=20)
y1 = np.linspace(0.75, 1.25, num=20)
l1 = []
l2 = []
l3 = []
l4 = []
for i in x1:
    l1.append([i, 0.75])
    l3.append([i, 1.25])

for j in y1:
    l2.append([1.25, j])
    l4.append([0.75, j])

OBS1 = [l1, l2, l3, l4]



#obstaculo 2
x1 = np.linspace(1.25, 1.75, num=20)
y1 = np.linspace(3.25, 3.75, num=20)
l1 = []
l2 = []
l3 = []
l4 = []
for i in x1:
    l1.append([i, 3.25])
    l3.append([i, 3.75])

for j in y1:
    l2.append([1.75, j])
    l4.append([1.25, j])

OBS2 = [l1, l2, l3, l4]



#obstaculo 3
x1 = np.linspace(2.25, 2.75, num=20)
y1 = np.linspace(2.25, 2.75, num=20)
l1 = []
l2 = []
l3 = []
l4 = []
for i in x1:
    l1.append([i, 2.25])
    l3.append([i, 2.75])

for j in y1:
    l2.append([2.75, j])
    l4.append([2.25, j])

OBS3 = [l1, l2, l3, l4]



#obstaculo 4
x1 = np.linspace(4.25, 4.75, num=20)
y1 = np.linspace(1.75, 2.25, num=20)
l1 = []
l2 = []
l3 = []
l4 = []
for i in x1:
    l1.append([i, 1.75])
    l3.append([i, 2.25])

for j in y1:
    l2.append([4.25, j])
    l4.append([4.75, j])

OBS4 = [l1, l2, l3, l4]



#obstaculo 5
x1 = np.linspace(2.75, 3.25, num=20)
y1 = np.linspace(0.75, 1.25, num=20)
l1 = []
l2 = []
l3 = []
l4 = []
for i in x1:
    l1.append([i, 0.75])
    l3.append([i, 1.25])

for j in y1:
    l2.append([2.75, j])
    l4.append([3.25, j])

OBS5 = [l1, l2, l3, l4]



#obstaculo 6
x1 = np.linspace(3.75, 4.25, num=20)
y1 = np.linspace(2.75, 3.25, num=20)
l1 = []
l2 = []
l3 = []
l4 = []
for i in x1:
    l1.append([i, 2.75])
    l3.append([i, 3.25])

for j in y1:
    l2.append([3.75, j])
    l4.append([4.25, j])

OBS6 = [l1, l2, l3, l4]


def distanciasPO(point):
    distMin = []
    indices = []
    temp = []
    tempDist = []

    l = 1
    for lado in OBS1:
        distancias = []
        for ponto in lado:
            d = round(np.linalg.norm(np.array(point) - np.array(ponto)), 2)
            distancias.append(d)
        minDist = min(distancias)
        temp.append([l, distancias.index(minDist)])
        tempDist.append(minDist)
        l += 1
    minTempDist = min(tempDist)
    distMin.append(minTempDist)
    indices.append(temp[tempDist.index(minTempDist)])
    temp = []
    tempDist = []

    l = 1
    for lado in OBS2:
        distancias = []
        for ponto in lado:
            d = round(np.linalg.norm(np.array(point) - np.array(ponto)), 2)
            distancias.append(d)
        minDist = min(distancias)
        temp.append([l, distancias.index(minDist)])
        tempDist.append(minDist)
        l += 1
    minTempDist = min(tempDist)
    distMin.append(minTempDist)
    indices.append(temp[tempDist.index(minTempDist)])
    temp = []
    tempDist = []

    l = 1
    for lado in OBS3:
        distancias = []
        for ponto in lado:
            d = round(np.linalg.norm(np.array(point) - np.array(ponto)), 2)
            distancias.append(d)
        minDist = min(distancias)
        temp.append([l, distancias.index(minDist)])
        tempDist.append(minDist)
        l += 1
    minTempDist = min(tempDist)
    distMin.append(minTempDist)
    indices.append(temp[tempDist.index(minTempDist)])
    temp = []
    tempDist = []

    l = 1
    for lado in OBS4:
        distancias = []
        for ponto in lado:
            d = round(np.linalg.norm(np.array(point) - np.array(ponto)), 2)
            distancias.append(d)
        minDist = min(distancias)
        temp.append([l, distancias.index(minDist)])
        tempDist.append(minDist)
        l += 1
    minTempDist = min(tempDist)
    distMin.append(minTempDist)
    indices.append(temp[tempDist.index(minTempDist)])
    temp = []
    tempDist = []

    l = 1
    for lado in OBS5:
        distancias = []
        for ponto in lado:
            d = round(np.linalg.norm(np.array(point) - np.array(ponto)), 2)
            distancias.append(d)
        minDist = min(distancias)
        temp.append([l, distancias.index(minDist)])
        tempDist.append(minDist)
        l += 1
    minTempDist = min(tempDist)
    distMin.append(minTempDist)
    indices.append(temp[tempDist.index(minTempDist)])
    temp = []
    tempDist = []

    l = 1
    for lado in OBS6:
        distancias = []
        for ponto in lado:
            d = round(np.linalg.norm(np.array(point) - np.array(ponto)), 2)
            distancias.append(d)
        minDist = min(distancias)
        temp.append([l, distancias.index(minDist)])
        tempDist.append(minDist)
        l += 1
    minTempDist = min(tempDist)
    distMin.append(minTempDist)
    indices.append(temp[tempDist.index(minTempDist)])
    temp = []
    tempDist = []

    return distMin, indices

def calculaCosseno(point, obst, target):
    u = np.array(obst) - np.array(point)
    v = np.array(target) - np.array(point)

    return 1-ssd.cosine(u,v)


