from time import time, sleep
import pybullet as p
import pybullet_data
import os

'''
urdf file in the same folder as that of the python script
'''
p.connect(p.GUI)
p.setGravity(0, 0, -10)


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


def load_obj(m):
    p.setGravity(0, 0, -10)
    no_drops = recur_fibo(m)
    for i in range(no_drops):
        robot1 = p.loadURDF(
            "sphere.urdf", [i*0.12, 0, 5])


wave = 1
while True:
    p.resetSimulation()
    p.loadURDF(os.path.join(
        pybullet_data.getDataPath(), "plane.urdf"), 0, 0, 0)
    load_obj(wave)
    for j in range(240):
        p.stepSimulation()
        sleep(1./240.)
    wave += 1
