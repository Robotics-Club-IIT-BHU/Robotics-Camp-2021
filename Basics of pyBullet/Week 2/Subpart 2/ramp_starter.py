import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)  
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
#these are the pre required conditions for the task.
ramp=p.loadURDF("wedge.urdf")
p.setGravity(0, 0, -10)
p.changeDynamics(ramp,-1,lateralFriction=0.5)

huskypos = [2, 0, 0.1]
husky = p.loadURDF("husky/husky.urdf", huskypos[0], huskypos[1], huskypos[2])

'''
1.print Number of Joints and joint info and state

2.Get the user input about the control function they 
want to simulate and see.(its upto you, it can be a string / int anything but just leave
a comment with the legend to your menu)

'''



#function to be filled to implement torque control
def Torque_control():

	# find this value to climb the ramp without sliping and topling
	optimal_torque_value = 0 
	
	'''
	this function should have the setJointMotorControl in TORQUE_CONTROL configuration
    with forc = optimal_force_value
    ''' 



#function to be filled to implement velocity control
def Velocity_control():
	# Keep a constant non zero value for maxForce and try getting the velocity that makes it climb the ramp.
	maxForce = 0 

	# find this value to climb the ramp without sliping
	optimal_velocity_value = 0 
	'''
	this function should have the setJointMotorControl in VELOCITY_CONTROL configuration
	with targetvelocity = optimal_velocity_value 
	'''



while (1):
	time.sleep(.01)
	'''
	1.Here call either the Torque_control function or Velocity_control 
	  function according to the initial user choice and apply the optimal velocity/Torque
	  to the motors that you have found by experimentation.

	2.print base state and velocity 100 iteration steps once.
	'''
	p.stepSimulation()





p.disconnect()