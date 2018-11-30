import matplotlib.pyplot as plt
import numpy as np
import math

def updatePerimeter(sphere):
    theta = np.linspace(0,2*math.pi,360)
    sphere["perimeter"]["xRange"] = [sphere["position"]["x"] + sphere["radius"]*math.cos(theta_inc) for theta_inc in
                                     theta]
    sphere["perimeter"]["yRange"] = [sphere["position"]["y"] + sphere["radius"] * math.sin(theta_inc) for theta_inc in
                                     theta]
    return sphere
def updateSphereGraph(sphere,colour):
    plt.plot(sphere["perimeter"]["xRange"], sphere["perimeter"]["yRange"],colour)
    plt.plot(sphere["position"]["x"], sphere["position"]["y"], 'rx')
    return plt
def updateGraphs(sphereList, graph):
    colours = ["b-","r-","g-"]
    count = 0
    graph.clear()
    for sphere in sphereList:
        updateSphereGraph(sphere,colours[count])
        count += 1
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    return plt
def updatePosition(sphere):
    sphere["position"]["x"] += sphere["t"]*sphere["velocity"]["x"] + 0.5*sphere["acceleration"]["x"]*math.pow(sphere["t"], 2)
    sphere["position"]["y"] += sphere["t"]*sphere["velocity"]["y"] + 0.5*sphere["acceleration"]["x"]*math.pow(sphere["t"], 2)
    sphere = updatePerimeter(sphere)
    return sphere

def updateAcceleration(sphereList):
    count = 0
    for active_sphere in sphereList:
        active_sphere["old_acceleration"] = active_sphere["acceleration"]
        active_sphere["acceleration"]["x"] = 0
        active_sphere["acceleration"]["y"] = 0
        tempList = sphereList[:count] + sphereList[count:]
        for other_sphere in tempList:
            active_sphere["acceleration"]["x"] += (other_sphere["position"]["x"] - active_sphere["position"]["x"])/10
            active_sphere["acceleration"]["y"] += (other_sphere["position"]["y"] - active_sphere["position"]["y"])/10
    return sphereList

def updateVelocity(sphere):
    sphere["velocity"]["x"] += 0.5 * (sphere["old_acceleration"]["x"] + sphere["acceleration"]["x"]) * sphere["t"]
    sphere["velocity"]["y"] += 0.5 * (sphere["old_acceleration"]["y"] + sphere["acceleration"]["y"]) * sphere["t"]
    return sphere

dt = 0.1

alphaSphere = {"mass": 1,
               "radius": 3,
               "velocity": {"x": 1, "y": 0},
               "acceleration": {"x": 0, "y": 0},
               "old_acceleration": {"x": 0, "y": 0},
               "position": {"x": 2, "y": 2},
               "t": dt,
               "perimeter": {"yRange": [], "xRange": []}
               }
alphaSphere = updatePerimeter(alphaSphere)
bravoSphere = {"mass": 1,
               "radius": 3,
               "velocity": {"x": -1, "y": 0},
               "acceleration": {"x": 0, "y": 0},
               "old_acceleration": {"x": 0, "y": 0},
               "position": {"x": -2, "y": -2},
               "t": dt,
               "perimeter": {"yRange": [], "xRange": []}
               }
bravoSphere = updatePerimeter(bravoSphere)

charlieSphere = {"mass": 1,
               "radius": 3,
               "velocity": {"x": 0, "y": 0},
               "acceleration": {"x": 0, "y": 0},
               "old_acceleration": {"x": 0, "y": 0},
               "position": {"x": 5, "y": -5},
               "t": dt,
               "perimeter": {"yRange": [], "xRange": []}
               }
charlieSphere = updatePerimeter(charlieSphere)


fig = plt.figure()
ax = fig.add_subplot(111)

all_spheres = [alphaSphere, bravoSphere, charlieSphere]

updateGraphs(all_spheres, ax)

total_time_passed = 0

while total_time_passed < 200:

    plt.pause(0.01)
    list(map(updatePosition,all_spheres))
    all_spheres = updateAcceleration(all_spheres)
    list(map(updateVelocity,all_spheres))
    updateGraphs(all_spheres, ax)

    total_time_passed += dt
plt.show()



