
import pybullet as p
import pybullet_data
import os
import time
'''
urdf file in the same folder as that of the python script
'''
p.connect(p.GUI)
p.loadURDF(os.path.join(pybullet_data.getDataPath(), "plane.urdf"), 0, 0, 0)
robot = p.loadURDF(
    "Week1_Subpart2_code1.urdf")
p.resetBasePositionAndOrientation(robot, [0, 0, 0], [0, 0, 0, 0.707])
p.setGravity(0, 0, 0)

while(True):
    p.stepSimulation()
