# Bonus Task 2

*Note: This task is an optional task and will be considered as a tiebreaker only if there is a tie among scores of participants. Attempt this task only if you have completed all previous tasks.*

## So, What is tougher than
|-|-|
|--|--|
| **Designing models with limited DOFs while traversing the whole Configuration without meeting any singularity.** | ![trig](1trig.jpg) |
| **Simulating Mutliple Tetrahedrals with Voxels constrained to each and making it look Deformable.** | ![triginf](38kveu.png) |

## SoftBody Simulation
New updates in pybullet allow us to simulate softbodies/Deformable bodies with high degree of precision. Like below ....

![output](media/softbody_example.gif)

...atleast for the most part of it.

## Getting Started.
This part of pybullet is not well documented so you may have to go into the realm of github issues to find something useful never the less hope fully below snippet and resource will give you the idea of how to go about spawning these softbodies.

```python
import pybullet as p
from time import sleep
import pybullet_data

physicsClient = p.connect(p.GUI)                        ## connect to server
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.resetSimulation(p.RESET_USE_DEFORMABLE_WORLD)         ## Flag to enable Deformable bodies

p.setGravity(0, 0, -10)

planeOrn = [0,0,0,1]#p.getQuaternionFromEuler([0.3,0,0])
planeId = p.loadURDF("plane.urdf", [0,0,-2],planeOrn)

ball1Id = p.loadSoftBody( "ball.obj",
                          simFileName = "ball.vtk", 
                          basePosition = [0,0,5], 
                          scale = 0.5, 
                          mass = 4,
                          useNeoHookean = 1,
                          NeoHookeanMu = 400,
                          NeoHookeanLambda = 600,
                          NeoHookeanDamping = 0.001,
                          useSelfCollision = 1,
                          frictionCoeff = .5,
                          collisionMargin = 0.001)      ## Loading softbody with given description

ball2Id = p.loadSoftBody( "ball.obj",
                          simFileName = "ball.vtk", 
                          basePosition = [0,0,0], 
                          scale = 0.5, 
                          mass = 4,
                          useNeoHookean = 1,
                          NeoHookeanMu = 400,
                          NeoHookeanLambda = 600,
                          NeoHookeanDamping = 0.001,
                          useSelfCollision = 1,
                          frictionCoeff = .5,
                          collisionMargin = 0.001)      ## Loading another softbody


p.setTimeStep(0.001)
p.setPhysicsEngineParameter(sparseSdfVoxelSize=0.25)    ## Setting a limit for the resolution of
                                                        ## voxel to increase performance and decrease accuracy



while p.isConnected():

  p.stepSimulation()                                    ## Run Run Run!!!
 
  p.setGravity(0,0,-10)

```
pybullet_data may not contain files for ball object(depends on how you installed pybullet and version) so you can simply download them from here and put it in the same folder as the python script.
- ball.obj
- ball.vtk
- ball.mtl
- uvmap.png

## Task - BBROY's *Greedy* Wife

Didn't value gold nor silver( coz they are rigid :/) for her necklace. She demanded for something more deformable (like here relationship) so BBRoy seeks out your help to make a necklace out of deformable objects(preferablly torus) attached together. Like so
<p align="center">
<img src="media/necklace.gif" />
</p>

You can choose
