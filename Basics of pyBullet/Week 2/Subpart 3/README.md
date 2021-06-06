# Subpart 3

<p align="center">
 <img src="https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/documentation2.jpg"><br>
</p>

## Input Management:

Its is quite important that we get to control the robot in our simulation manually.Even a manual override or interrupt is required for any autonomous system.Hence,in this part you will learn how to control a robot in PyBullet using Keyboard/Mouse.
First lets see a demo of this- **Run the [car.py](https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%203/car.py)** file provided above.(Don't worry about understanding the code, you will understand the code after referring to the documentation mentioned below).In this example you can control the car to go forward/backward using up/down arrows.

There are two simple functions for Input Management,namely
<div align = "center">
 
[getKeyboardEvents,getMouseEvents](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.jvkackps3ev0)


</div>

## External Force/Torque:
_Q.Why do we really need to simulate a external force on the robot ??_

_Ans: To kick robots and bully them and have fun !! why,else ?:-)_

<p align="center">
 <img width = "400" height = "300" src="https://media.giphy.com/media/3rgXBINepaeqSr1OfK/giphy.gif">
 <img width = "400" height = "300" src="https://cdn.zmescience.com/wp-content/uploads/2016/02/xyDeq5VeiILHq.gif">
</p>


Well on a serious note,one of the key challenge to overcome in transfering a robot from simulation to reality is the undezireable and unpredictable disturbance caused in the real world.The source of these disturbances that hinders the motion of our robot is generally a force or torque.Thus, as robotic professionals it is important that we make robot controllers that are **robust,agile and versatile**.So, we should learn to simulate such undezirable conditions in our simulations aswell.

The function(s) that enables you to design such forces are designed below: 

<div align = "center">

[applyExternalForce/Torque](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.mq73m9o2gcpy)

</div>

## **Task 1**

In the code [car.py](https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%203/car.py) shared above,add
these additional functionalities,

1. Right and Left turn user control through **differential drive** method.
2. The car should rotate about its axis of symmetry when the user inputs the letter **r**.
3. Should increase the velocity/torque of all the motors by one unit if the user inputs the letter **a** ie the current value of motion , is to be increamented **by a unit magnitude**, and consequtively when you press a forward or backward the car will be moving in the new updated value.(for eg, if current targetvelocity=3 and -3 for forward and backward respectively, it is expected to be updated to  targetVelocity = 4 and -4 according to the direction case,when a is pressed)

## Constraints:

Unlike the constraints mentioned in the earlier part that describes the internal motion capablities of a robot,there might be scenarios where we need to apply constraints in between the robot and a unit in the environment and simulate such constrained conditions

<p align="center">
 <img width = "460" height = "250" src="https://thumbs.gfycat.com/MajorWeeKilldeer-size_restricted.gif">
</p>

For example a robot walking around in a given circular track as depicted above.In the above arrangement thought the robot is a spatial body that can move in the 3d space independently with a dof = 6,we have constrained it to a central pivot using a bar to make it walk in a circular track.

The functions that enables you to design such constraints are listed below:

<div align = "center">

[createConstraint, removeConstraint](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.fq749wu22x4c)
 
[changeConstraint](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.fq749wu22x4c)

[getNumConstraints](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.hsbb69vwmyl0)

[getConstraintUniqueId](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.hsbb69vwmyl0)

[getConstraintInfo/State](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.zjkkp84f52f)

</div>





**Bonus Task**

Based on the topics **Constraints** and **external Force**, you are expected to build a **NEWTON's CRADLE**.

<p align="center">
 <img width = "300" height = "300" src="https://gifimage.net/wp-content/uploads/2017/08/newtons-cradle-gif-1-1.gif">
 </p>

Use the [sphere.urdf from PART 1,Subpart 3](https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part1/Subpart%203/sphere.urdf) as the bobs of the pendulums and use the in-built cube urdf as pins.The pins should be constrained and held **static** in a single point in space and the bob is to be kept at a constant length,suspended from the pin.The simulation should start with a **external force acting on the COM** of one of the bobs in the extreme positon.

**Note:** Its upto you to decide the number of spheres,suspension length,point of suspension,magnitude of initial force,etc.



