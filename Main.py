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
    colours = ["b-","r-","g-", "y-"]
    count = 0
    graph.clear()
    for sphere in sphereList:
        updateSphereGraph(sphere,colours[count])
        count += 1
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    return plt

def updatePosition(sphere):
    sphere["position"]["x"] += sphere["t"]*sphere["velocity"]["x"] + 0.5*sphere["acceleration"]["x"]*math.pow(sphere["t"], 2)
    sphere["position"]["y"] += sphere["t"]*sphere["velocity"]["y"] + 0.5*sphere["acceleration"]["x"]*math.pow(sphere["t"], 2)
    sphere = updatePerimeter(sphere)
    return sphere

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def updateAcceleration(sphereList):
    count = 0
    spring_constant = 5e15
    damping_factor = 0.75
    for active_sphere in sphereList:
        active_sphere["old_acceleration"] = active_sphere["acceleration"]
        active_sphere["acceleration"]["x"] = 0
        active_sphere["acceleration"]["y"] = 0
        tempList = sphereList[:count] + sphereList[count+1:]
        for other_sphere in tempList:
            x_seperation = (other_sphere["position"]["x"] - active_sphere["position"]["x"])
            y_seperation = (other_sphere["position"]["y"] - active_sphere["position"]["y"])
            [total_seperation,vector_angle] = cart2pol(x_seperation,y_seperation)
            acceleration_scalar = 6.67e-11*other_sphere["mass"]/math.pow(total_seperation,2)
            active_sphere["acceleration"]["x"] += acceleration_scalar * math.cos(vector_angle)
            active_sphere["acceleration"]["y"] += acceleration_scalar * math.sin(vector_angle)
            if total_seperation < 2:
                overlap = 2 - total_seperation
                #print("overlapping")
                repel_force = damping_factor * spring_constant*overlap/active_sphere["mass"]
                #print(repel_force)
                active_sphere["acceleration"]["x"] -= math.cos(vector_angle) * repel_force
                active_sphere["acceleration"]["y"] -= math.sin(vector_angle) * repel_force
                #print(active_sphere["acceleration"]["x"],active_sphere["acceleration"]["y"])
        count += 1
    return sphereList

def updateVelocity(sphere):
    sphere["velocity"]["x"] += 0.5 * (sphere["old_acceleration"]["x"] + sphere["acceleration"]["x"]) * sphere["t"]
    sphere["velocity"]["y"] += 0.5 * (sphere["old_acceleration"]["y"] + sphere["acceleration"]["y"]) * sphere["t"]
    return sphere

dt = 0.005

alphaSphere = {"mass": 1e12,
               "radius": 1,
               "velocity": {"x": 3, "y": 0},
               "acceleration": {"x": 0, "y": 0},
               "old_acceleration": {"x": 0, "y": 0},
               "position": {"x": 2, "y": 2},
               "t": dt,
               "perimeter": {"yRange": [], "xRange": []}
               }
alphaSphere = updatePerimeter(alphaSphere)
bravoSphere = {"mass": 1e12,
               "radius": 1,
               "velocity": {"x": -3, "y": 0},
               "acceleration": {"x": 0, "y": 0},
               "old_acceleration": {"x": 0, "y": 0},
               "position": {"x": -2, "y": -2},
               "t": dt,
               "perimeter": {"yRange": [], "xRange": []}
               }
bravoSphere = updatePerimeter(bravoSphere)

charlieSphere = {"mass": 1e12,
               "radius": 1,
               "velocity": {"x": 0, "y": 0},
               "acceleration": {"x": 0, "y": 0},
               "old_acceleration": {"x": 0, "y": 0},
               "position": {"x": 2, "y": -2},
               "t": dt,
               "perimeter": {"yRange": [], "xRange": []}
               }
charlieSphere = updatePerimeter(charlieSphere)

deltaSphere = {"mass": 1e12,
               "radius": 1,
               "velocity": {"x": 0, "y": 0},
               "acceleration": {"x": 0, "y": 0},
               "old_acceleration": {"x": 0, "y": 0},
               "position": {"x": -2, "y": 2},
               "t": dt,
               "perimeter": {"yRange": [], "xRange": []}
               }
deltaSphere = updatePerimeter(deltaSphere)


fig = plt.figure()
ax = fig.add_subplot(111)

all_spheres = [alphaSphere, bravoSphere, charlieSphere, deltaSphere]

updateGraphs(all_spheres, ax)

total_time_passed = 0

while total_time_passed < 20:

    plt.pause(0.005)
    list(map(updatePosition,all_spheres))
    all_spheres = updateAcceleration(all_spheres)
    list(map(updateVelocity,all_spheres))
    updateGraphs(all_spheres, ax)

    total_time_passed += dt
    #print(total_time_passed)
plt.show()


