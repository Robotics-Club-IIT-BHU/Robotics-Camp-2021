
import pybullet as p
import pybullet_data
import os
import time
'''
urdf file in the same folder as that of the python script
'''

'''
these comands are explained in detail in the next subpart
for now u can directly use it to visualize the model
'''

numObjects = 50
y = 0

p.connect(p.GUI)
p.loadURDF(os.path.join(pybullet_data.getDataPath(), "plane.urdf"), 0, 0, 0)
while(True):
    for i in range(numObjects):
        robot = p.loadURDF("sphere.urdf", [0, i*0.1, 5])
        p.resetBasePositionAndOrientation(
            robot, [0, i*0.1, 5], [0, 0, 0, 0.707])
        while(y <= 19.6):
            p.setGravity(0, 0, -0.002)

    # Joint_1 = p.addUserDebugParameter("range", -3.14, 3.14)

    while(True):
        p.stepSimulation()
    time.sleep(2)

    # print(os.getcwd())
