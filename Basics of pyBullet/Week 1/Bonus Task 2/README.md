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
- [ball.obj](https://raw.githubusercontent.com/bulletphysics/bullet3/master/data/ball.obj) : Obj file describes the softbody as a collection of points.
- [ball.vtk](https://raw.githubusercontent.com/bulletphysics/bullet3/master/data/ball.vtk) : Vtk file describes the softbody as a collection of Voxels.
- [ball.mtl](https://raw.githubusercontent.com/bulletphysics/bullet3/master/data/ball.mtl) : Mtl file describes the texture of the deformable object by assiging a small section of the texture to individual elements.
- [uvmap.png](https://raw.githubusercontent.com/bulletphysics/bullet3/master/data/uvmap.png): uvmap file is a specific texture loaded which is used in ball.mtl (else it is not a normal format of file needed for softbody).

## Task - BBROY's *Greedy* Wife

Didn't value gold nor silver( coz they are rigid :/) for her necklace. She demanded for something more deformable (like here relationship) so BBRoy seeks out your help to make a necklace out of deformable objects(preferablly torus) attached together. Like so
<p align="center">
<img src="media/necklace.gif" />
</p>

You can choose any combination of deformable objects to link together due to there geometry and not creating any joints or constrains ( that is if you spawn them at the right place and right orientation you should be done).

The more beatiful you make the necklace the more pleased BBRoy'S wife would be, giving you full grade in all the circutal subjects hereafter :). 


### References
- #### Data : There is sparse resources for this that work. so best is to take the official data available at [**[link]**](https://github.com/bulletphysics/bullet3/tree/master/data) Most of the obj, vtk will work just fine on loading else there maybe two reasons 
 1. Newer or older versions of pybullet which don't support softbody or has many filters restricting many softbodies from loading , Solution `pip install pybullet==3.1.5` we have tested out most of the vtk files to have run with this version of pybullet installed through pip. 
 2. You are using files from `pybullet_data` which has partial or old files hence we would recommend to download from [here](#Data) and rename file to use it as a normal file in the same directory.
- #### Scripts : most of them are available in the [official pybullet repository](https://github.com/bulletphysics/bullet3/blob/master/examples/pybullet/examples/) to be more specific you can take a look into atleast these
1. [deformable_sphere.py](https://github.com/bulletphysics/bullet3/blob/master/examples/pybullet/examples/deformable_sphere.py)
2. [deformable_torus.py](https://github.com/bulletphysics/bullet3/blob/master/examples/pybullet/examples/deformable_torus.py)
for these scripts you can find data [here](#Data)
