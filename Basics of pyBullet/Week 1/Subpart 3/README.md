# Subpart 3

Getting to know about robot models, its time to do some serious simulation !!

## Note:
   As a prescribed text we share the [PyBullet_Quickstart_Guide](https://github.com/NiranthS/Pybullet-Camp/blob/master/Part1/Subpart%203/PyBullet_Quickstart_Guide.pdf) for quick reference.It contains almost all the functions and the necassary details for using Pybullet,in short its like your bible for this course.Thus, through out this camp it is advised you constanly refer this for better understanding.

## Starter code:
Moving on,here we will see a basic code in PyBullet and understand the functions used in it.
```python
import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)
for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)
p.disconnect()
```
We will go through each line of the code and understand what it does,
1. First we import the required libraries i.e. pybullet, time and pybullet_data
2. **connect**
* After importing the PyBullet module, the first thing to do is 'connecting' to the physics simulation. PyBullet is designed around a client-server driven API, with a client sending commands and a physics server returning the status. PyBullet has some built-in physics servers: DIRECT and GUI. Both GUI and DIRECT connections will execute the physics simulation and rendering in the same process as PyBullet.
* The connect function returns a physics client id.
* The DIRECT connection sends the commands directly to the physics engine, without using any transport layer and no graphics visualization window, and directly returns the status after executing the command.
* The GUI connection will create a new graphical user interface (GUI) with 3D OpenGL rendering, within the same process space as PyBullet.
3. **setAdditionalSearchPath** is used to add pybullet_data to the path which contains many examples, urdf files, etc.
4. **setGravity**:By default, there is no gravitational force enabled. setGravity lets you set the default gravity force for all objects.
The setGravity input parameters are: (no return value):


parameter type  | Name | type | Description
--- | --- | --- | ---
required  | gravityX | float | gravity force along the X world axis
required  | gravityY | float | gravity force along the Y world axis
required  | gravityZ | float | gravity force along the Z world axis
optional  | physicsClientId | int | if you connect to multiple physics servers, you can pick which one.

5. **loadURDF**: The loadURDF will send a command to the physics server to load a physics model from a Universal Robot Description File (URDF).

Some important arguments of loadURDF are:

parameter type  | Name | type | Description
--- | --- | --- | ---
required  | fileName | string | a relative or absolute path to the URDF file on the file system of the physics server.
optional  | basePosition | vec3 | create the base of the object at the specified position in world space coordinates [X,Y,Z]. Note that this position is of the URDF link position. If the inertial frame is non-zero, this is different from the center of mass position. Use resetBasePositionAndOrientation to set the center of mass location/orientation.
optional  | baseOrientation | vec4 | create the base of the object at the specified orientation as world space quaternion [X,Y,Z,W]. See note in basePosition.

6. We store the initial position of our urdf file in the variable cubsStartPos.

7. We store the initial Quaternion orientation of our urdf file in cubeStartOrientation
**(More details about Quaternions will be given in Part 2 of the camp)**

8. We import our r2d2 robot urdf file in the desired position and orientation.

9. **stepSimulation**:stepSimulation will perform all the actions in a single forward dynamics simulation step. The default timestep is 1/240 second, it can be changed using the setTimeStep or setPhysicsEngineParameter API.

10.**getBasePositionAndOrientation**:getBasePositionAndOrientation reports the current position and orientation of the base (or root link) of the body in Cartesian world coordinates. The orientation is a quaternion in [x,y,z,w] format.
The arguments of getBasePositionAndOrientation are:

parameter type  | Name | type | Description
--- | --- | --- | ---
required  | objectUniqueId | int | object unique id, as returned from loadURDF.
optional  | physicsClientId | int | if you are connected to multiple servers, you can pick one.

11.**disconnect**: You can disconnect from a physics server. A 'DIRECT' or 'GUI' physics server will shutdown. A separate (out-of-process) physics server will keep on running. See also 'resetSimulation' to remove all items.

## Task for the part

In this task, you are expected to simulate the following conditions using the functions described above.

**Task - 1 - Accelerating Gravity !!**

1. **Total_Time_Step:** Infinite
2. **Gravity:**
along a direction 1/√2 i + 1/√2 j + 0 k , that increases from a magnitude of 0 linearly to a magnitude of 9.8 m/s^2 and resets to 0 and continues the cycle.(*Hint:Gravity should be a function that updates itself every time step of the simulation.*)

3. **Bodies in the simulation:**
Import the given [sample.urdf](https://github.com/NiranthS/Pybullet-Camp/blob/master/Part1/Subpart%202/sample.urdf) file at the position [2,2,1] and [dabba.urdf](https://github.com/NiranthS/Pybullet-Camp/blob/master/Part1/Subpart%203/dabba.urdf) file at [0,0,1] position. 

**Task for Bonus Score - Fibanocci Rainfall.**

   Try simulating a rainfall using [sphere.urdf](https://github.com/NiranthS/Pybullet-Camp/blob/master/Part1/Subpart%203/sphere.urdf) as the raindrops. The rainfall should be in such a way that every wave of rainfall should have a Fibonocci number of raindrops. The spheres should start falling from a specified height with a gravity -10 m/s^2. The spheres should equally space along the X-axis during the start of the wave.
   
1. **Timesteps_per_wave:** 10,000
2. **Height of release:** 5 units from the ground along +z axis
3. **Last term of Fibanocci rainfall:** well, find it !

eg:

Let F(i) be the ith Fibonacci term.
Hence, the i th wave of the rainfall should have F(i) spheres falling freely.Once, the drops reach the ground the simuation gets reset and starts the next wave.(i+1 th wave with F(i+1) drops and so on.. )





