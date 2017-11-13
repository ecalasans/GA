import numpy as np
import genetics
import obstaculos
import scipy.spatial.distance as ssd

a = np.array([0, 0])
b = np.array([0,4])
c = np.array([4, 6.9])

u = b-a
v = c-a

print np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))
print 1-ssd.cosine(u, v)

print np.rad2deg(np.arccos(1-ssd.cosine(u,v)))
