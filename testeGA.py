import numpy as np
import genetics
import obstaculos
import scipy.spatial.distance as ssd

u = np.array([0,0,0,3])
v = np.array([0,0,3,3])

print np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))

print np.rad2deg(np.arccos(1-ssd.cosine(u,v)))

