# Subpart 1
## Collisions
What is a collision?
* When a robot collides with a workpiece/a part of itself, then it is known as a collision.
* We need functions in the simulator that detects this collision and brings the robot to an emergency stop.
<p align="middle">
 <img  width="300" height="300" src="https://github.com/NiranthS/Media_files/blob/master/with_collision1.gif"><br>
</p>

<p align="middle">
A cube with collision
</p>

<p align="middle">
 <img  width="300" height="300" src="https://github.com/NiranthS/Media_files/blob/master/without_collision.gif"><br>
</p>

<p align="middle">
 A cube without collision
</p>

## Self-collision:
* Self-collision is the collision among different links of a robot.
* By default, collision detection is enabled between different dynamic moving bodies. Self-collision between links of the same body can be enabled using flags such as 'URDF_USE_SELF_COLLISION' flag in loadURDF.
* Also, the urdf must have a collision model for the robot, you can refer to dabba.urdf and sphere.urdf to understand the inertial and collision tags on your own. More details on this can again be found in the same resource shared in subpart 2 of Part -1.

## Getting an image from camera

<p align="middle">
 <img  width="350" height="300" src="https://pics.me.me/controlling-your-robot-using-a-camera-vs-autonomous-code-it-39558286.png"><br>
</p>

* An image from a camera in the simulator has lots of uses in Computer Vision-based controllers, Object detection, etc.
* There are **3 important functions** to get an image by placing camera anywhere in the simulator:
1. **computeViewMatrix**:

parameter type  | Name | type | Description
--- | --- | --- | ---
required  | cameraEyePosition | vec3, list of 3 floats | eye position in Cartesian world coordinates
required  | cameraTargetPosition | vec3, list of 3 floats | position of the target (focus) point, in Cartesian world coordinates
required  | cameraUpVector | vec3, list of 3 floats | up vector of the camera, in Cartesian world coordinates
optional  | physicsClientId | int | unused,added for API consistency

* cameraEyePosition is the position where the camera is to be placed.
* cameraTargetPosition is the focal point of the camera
* cameraUpVector is a 3D vector that points in the general direction of “up” from the camera.
* Output is the 4x4 view matrix, stored as a list of 16 floats.

2.**computeProjectionMatrixFOV**

parameter type  | Name | type | Description
--- | --- | --- | ---
required  | fov | float | field of view
required  | aspect | float | aspect ratio
required  | nearVal | float | near plane distance
required  | farVal | float | far plane distance
optional  | physicsClientId | int | unused,added for API consistency

* field of view:  the field of view is that part of the world that is visible through the camera at a particular position and orientation in space; objects outside the FOV when the picture is taken are not recorded in the photo.
* aspect ration: the ratio of the width to the height of an image or screen.
* near plane distance: The distance from the camera to the nearest object in the scene.
* far plane distance: The distance from the camera to the farthest object in the scene.

3. **getCameraImage**

* View Matrix and Projection matrix computed above are used in this function to set the parameters of the camera
* You can refer to this documentation for a description of this function:
<div align="center">
 
 [getCameraImage](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.u1jisfnt6984)
  
</div>

* Here is an example for your understanding of the above functions [camera_example.py](https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part3/Subpart1/camera_example.py)
* Try to change different parameters in the above example and see how the image changes.

## Task for the part

* In this task you are expected to capture a **frame from the perspective of the robot car *husky***. As a continuation to Task -1 of Subpart3 of Part-2, where you control the car using arrow keys, add another user input 'c' such that when a user triggers 'c', an image from the camera placed on the car pointing along the direction of the car should be displayed as a frame,say using _cv2.imshow()_.ie take a picture from the car's *First Person View* perspective(image should show whatever is infront of the car,from what the *driver* sees,in simple terms.)

* So,if you consider the gif shown in *collision part*, your image will be having a green box,as that is what the **"car is seeing"**.

* OpenCV functions are useful to do any changes to the image.

**You can even try to implement problem statement of [Vision](https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part3/Subpart1/Vision%20final%20PS.docx) in the simulator,but is not mandatory for the assesment.**


