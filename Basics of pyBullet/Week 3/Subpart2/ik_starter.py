import pybullet as p
import pybullet_data
import os
import time

file_name = "2R_planar_robot.urdf"
p.connect(p.GUI)

p.loadURDF(os.path.join(pybullet_data.getDataPath(), "plane.urdf"), 0, 0, 0)
robot = p.loadURDF(file_name)
p.resetBasePositionAndOrientation(robot, [0, 0, 0.05], [0, 0, 0, 0.707])

p.setGravity(0,0,-10)

'''
Note:

*these are the two end point of the line segment you want to 
 draw,so after finding the line segment you want to trace change 
 the two point below.

*the function addUserDebugLine just draws the line segment joining
point_A and point_B 

'''

point_A = [0,1,0]
point_B = [0,1,1]
p.addUserDebugLine(point_A,point_B,[1,0,0],2)

l1 = 0 #update the length of link-1,from the urdf
l2 = 0 #updare the length of link-2,from the urdf

def Forward_kinematics(angle_1,angle_2):

	'''
	This function should do the necessary trignometric 
	calculations using angle_1,angle_2,l1,l2 and resturn the [0,y,z] as the robot
	works space is the y-z plane
	'''
	y=0 # calculate y
	z=0 # calculate z
	return [0,y,z]

def Inverse_kinematics(target):
	'''
	This function should do the necessary trignometric 
	calculations using y ,z,l1,l2 and return angle_1 and angle_2 to 
	reach a given target of the form [0,y,z],as the robot 
	works space is th y-z plane.
	'''
	angle_1=0#calculate angle_1
	angle_2=0#calculate angle_2
	return angle_1,angle_2

'''
Write the equation of the line you are going to follow:-
Example, 

*it might be of the for z = m*y + c, so in the
 while loop below increament y = y + dy and find new z
 and give the target ie [0,y,z] to the Inverse_Kinematics 
 function.

*so trace the line from point_A to point_B and reset position 
 to point_A and continue the same process infinitely.  

'''

while(True):

	
	angle_1,angle_2  = Inverse_kinematics([0,1,1])
	

	p.setJointMotorControl2(bodyIndex=robot,
                            jointIndex=0,
                            controlMode =p.POSITION_CONTROL,
                            targetPosition=angle_1,
                            force=500)

	p.setJointMotorControl2(bodyIndex=robot,
                            jointIndex=1,
                            controlMode =p.POSITION_CONTROL,
                            targetPosition=angle_2,
                            force=500)

	p.stepSimulation()
