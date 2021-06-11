# Subpart 2

Official documentation is sometimes the best place to get the required information. **The PyBullet Example Code Directory given below consists of example implementations for all the functions given in the documentation(make good use of it!!)**
<div align ="center">

[Pybullet Example Code Directory](https://github.com/bulletphysics/bullet3/tree/master/examples/pybullet/examples)

</div>

Sometimes you can find the information you need in Stackoverflow without referring to the documentation.

<p align="center">
 <img  width="350" height="400" src="https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/documentation%201.png"><br>
</p>



## Robot orientation and position (for mobile robot):
Another important information about a robot or specifically a **mobile robot** is its absolute **position and orientation** in the simulation world. In real-world terms, it is something like the GPS position, map cordinates, compass readings. In a nutshell, we need data to get a sense of position and localization. The term orientation, however, comes into the picture when we consider **frame** based tracking of the space over position-only 3d space. Thus, if we consider a global frame with the i,j, and k directions defined, then the amount of **inclination** about all the axes (_ie. rotation ) of a **local frame** taken on the robot gives its orientation.

## Robot Orientation Formats:

**Euler angles:** 

This the most intuitive and straight forward approach towards accounting the changes in orientation with respect to a global frame.
1. [Check this video for a better picture](https://www.youtube.com/watch?v=q0jgqeS_ACM)
2. Though these angles might look like they serve the purpose, there is a very serious problem that they hold called **gimbal lock**. The solution to this will be the next type of orientation description. More details about the problem are in the links below,
   1. [Axis Angles, Euler Angles and Gimbal Lock](https://youtu.be/Mm8tzzfy1Uw)
   2. [Gimbal lock](https://www.youtube.com/watch?v=zc8b2Jo7mno)
   3. [Apollo 13 and gimbal lock](https://www.youtube.com/watch?v=OmCzZ-D8Wdk)
  
**Quaternions:**

_Q.Well, what could be an effective soltuion for a simple angle tracking problem?_ 

_You are absolutely right if complex numbers were your answer !!_

<p align="center">
<img  width="300" height="300" src="https://media2.giphy.com/media/Cn76Lj0aEw1dm/giphy.gif"><br>
</p>


We do hear you screaming that, but hold on...Quaternion is perhaps one of the most beautiful formulations in geometry.
Rather than we explaining something that is **"simply complex"**, we leave it to this beautiful work from the channel 3Blue1Brown.

<div align="center">

[Visualizing quaternions (4d numbers) with stereographic projection](https://www.youtube.com/watch?v=d4EgbgTm0Bg)

</div>
<p align="center">
<img src="https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%202/quat1.jpg"><br>
</p>

## Robot Motion Control:

Until now we havent addressed one of the primary control needs of a mobile robot, which is to control the indepedent joints of the robots.Motors as we all are aware of, are machines that induce some form of motion, by creating a **torque** in the case of rotational motors and a force in the case of linear motor/actuators.Thus,motors are the **motion causing elements** of a robot.However, in simulation the details,specifications and design of a given motor type is insignificant and we only need the **physical properties of that motor we want to mimic**.


So, every motor in Pybullet is characterized by the maximum velocity and maximum force (it is generalized velocity and force as in lagrangian mechanics and hence it is angular velocity and torque in rotational motors) it can exert.Every **joint by default has a motor** attached to it and hence we just need to give the **motor's desired position / velocity / torque** to control them.**setMotorControl2** is an import function which is used to control the motors in our robot by providing the desired velocity and max force to use to reach the desired velocity


<div align="center">
 
[setMotorControl2](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.jxof6bt5vhut)

</div>

**Note:** We will be ellaborately discussing about the control types in the upcoming parts, for now use the 

__*VELOCITY_CONTROL/TORQUE_CONTROL*__ as the third argument when you use this fuction for **continuous rotation motors** to give the desirable velocity/torque. 

_**POSITON_CONTROL**_ is analogous to using a servo motor were you give the angle that you want the motor shaft to be at.

## **Task of the part:**
The task for this part will be to make the husky car climb a wedge using torque and velocity control.The overall task is broadly classified into two parts.

1.**Extracting information from the bot:** 
    
   1. You are expected to print the number of joints and joint information of all the joints once during the begining of the code.
   
   **Note:** Not all joints are useful for the motion task.Based on the joint info you are expected to use the joints correspoding the wheels for the setJointMotorcontrol function.
     
   2. Print the Base link state information and Base velocity,once every 100th iteration step of the simulation.
     
2.**Climbing up the wedge:**

  1. Write 2 functions to implement **Torque control** and **Velocity control** individually.Based on the user input    select one among the above control functions during the begining of the program.
  
  2. For the given conditions try getting the optimal value of **force** for **Torque control function** and **Velocity** for **Velocity control function** and initialize it in the function.The optimal value of force and velocity should enable the robot to climb up the ramp without sliping and it should not come out of the ramp from its sides.

<p align="center">
<img height ="400" width = "400" src="https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%202/car.gif"><br>
</p>

The starter code with the necessary friction values of surfaces and the wedge urdf is available here. - [ramp_starter.py](https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%202/ramp_starter.py) 

The hardware resource files with [wedge.urdf](https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%202/wedge.urdf) and [ramp2.stl](https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%202/ramp2.stl) is to be kept in the same directory as ramp.py




   


