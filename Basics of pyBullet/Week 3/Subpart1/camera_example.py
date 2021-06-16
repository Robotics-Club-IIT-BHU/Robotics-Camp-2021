import matplotlib.pyplot as plt
import numpy as np
import pybullet as p
import time
import pybullet_data
import cv2
direct = p.connect(p.GUI)  #, options="--window_backend=2 --render_device=0")
#egl = p.loadPlugin("eglRendererPlugin")

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF('plane.urdf')
p.loadURDF("r2d2.urdf", [0, 0, 1])
p.loadURDF('cube_small.urdf', basePosition=[0.0, 0.0, 0.025])
cube_trans = p.loadURDF('cube_small.urdf', basePosition=[0.0, 0.1, 0.025])
p.changeVisualShape(cube_trans, -1, rgbaColor=[1, 1, 1, 0.1])
width = 512
height = 512

fov = 60
aspect = width / height
near = 0.02
far = 5

view_matrix = p.computeViewMatrix([0, 0, 2], [0, 0, 0], [1, 0, 0])
projection_matrix = p.computeProjectionMatrixFOV(fov, aspect, near, far)

# Get depth values using the OpenGL renderer
images = p.getCameraImage(width,
                          height,
                          view_matrix,
                          projection_matrix,
                          shadow=True,
                          renderer=p.ER_BULLET_HARDWARE_OPENGL)
rgb_opengl = np.reshape(images[2], (height, width, 4)) * 1. / 255.
cv2.imshow('rgb',rgb_opengl)
cv2.waitKey(0)
cv2.destroyAllWindows()
