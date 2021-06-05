# SHIVANSH DUBEY, 20095107

import pybullet as p
import pybullet_data
import os
import time

p.connect(p.GUI)
p.loadURDF(os.path.join(pybullet_data.getDataPath(), "plane.urdf"), 0, 0, 0)
robot1 = p.loadURDF(
    "dabba.urdf")
robot2 = p.loadURDF(
    "sample.urdf")
p.resetBasePositionAndOrientation(robot1, [0, 0, 1], [0, 0, 0, 0.707])
p.resetBasePositionAndOrientation(robot2, [2, 2, 1], [0, 0, 0, 0.707])

i = 0
while(True):
    while(i > -1):
        y = 0
        p.resetBasePositionAndOrientation(
            robot1, [0, 0, 1], [0, 0, 0, 0.707])
        p.resetBasePositionAndOrientation(
            robot2, [2, 2, 1], [0, 0, 0, 0.707])
        while(y <= 1):
            x = i + 9.8*y
            p.setGravity(x, x, 0)
            p.stepSimulation()
            time.sleep(1/240)
            y += (1/240)
        i += 1
