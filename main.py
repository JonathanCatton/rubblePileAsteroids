import matplotlib.pyplot as plt
import numpy as np
import math
alphaSphere = {"mass": 1,
               "radius": 5,
               "velocity": {"x": 0,"y": 0},
               "acceleration": {"x": 0,"y": 0},
               "position": {"x": 1.5,"y": -3},
               "perimeter": {"yRange": [],"xRange": []}
               }

theta = np.linspace(0,2*math.pi,360)
for theta_increment in theta:
    alphaSphere["perimeter"]["xRange"].append(
        alphaSphere["position"]["x"] + alphaSphere["radius"] * math.cos(theta_increment))
    alphaSphere["perimeter"]["yRange"].append(
        alphaSphere["position"]["y"] + alphaSphere["radius"] * math.sin(theta_increment))

plt.plot(alphaSphere["perimeter"]["xRange"], alphaSphere["perimeter"]["yRange"])
plt.plot(alphaSphere["position"]["x"],alphaSphere["position"]["y"], 'rx')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()
