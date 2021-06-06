# Subpart 1
<p align="center">
 <img  width="350" height="400" src="https://beyondexcelmodeling.com/images/FinModAna-02-What-is-Financial-Modeling.010.jpg"><br>
</p>

  In accordance to wich this subpart we will be introducing you to some of the basic definitions and fundamental concepts about the robot geometry and dynamics. The implementation of this theory in the simulation will be available in the sucessive subparts.


## The robot model:-
  As mentioned earlier we tend to model robots based on links and joints. An important point to note will be that we are limiting ourselves to **rigid bodies**_-ie no form of internal deformation is allowed/included_.This assumption drastically simplified our mathematical model and is also applicable to the vast majority of robots present.


## Robot Configuration/State:
  It becomes crucial to represent the robot in 3d space in an effective way as it greatly determines the design and performance of our controller and other higher-level control modules of the robot. 
  
**Configuration**: The configuration of a robot is a complete specification of the position of every point of the robot.  The n-dimensional space containing all possible configurations of the robot is called the configuration space (C-space). The configuration of a robot is represented by a point in its C-space.

for eg,

<p align="center">
 <img  width="600" height="350" src=https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%201/c_space.jpg>
</p>

## Degree of freedom(dof):
### The general defn:

<div align="center">

      degrees of freedom = (sum of freedoms of the bodies) - (number of independent constraints)

</div>

### In Robotics:
 
 In robotics, the **Degree of Freedom** represents the minimum number (n) of real-valued coordinates needed to represent the configuration is the number of degrees of freedom (DOF) of the robot.The motion determining elements in a robot is its **joints**. Hence, all the joints in a given robot collectively decide a robot's possible motion. So, every individual joint has a DOF according to the general defn above and the robot's DOF calcuted by Grubler's Formula.

The table below summarizes the DOF of each joint and how it has been constrained to move.

<p align="center">
 <img  width="620" height="290" src="https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%201/joint.png"><br>
</p>
 
### Grubler's Formula:
  The number of degrees of freedom of a mechanism with links and joints can be calculated using **Grubler's formula**, which can be easily derived from the above general definition of DOF.
  
Consider a mechanism consisting of N links, where the ground is also regarded as a link.

Let 
* J be the number of joints,
* m be the number of degrees of freedom of a rigid body (m = 3 for planar mechanisms and m = 6 for spatial mechanisms), 
* fi be the number of freedoms provided by joint i, and 
* ci be the number of constraints provided by joint i, where fi + ci = m for all i. Then

<p align="center">
 <img  width="600" height="300" src="https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%201/dof.jpg"><br>
</p>

**Note:** This formula holds only if all joint constraints are independent. If they are not independent then the formula provides a lower bound on the number of degrees of freedom.

**Eg:**

Let's consider a 4R serial planar robot arm as shown in the image below,
<p align="center">
<img  width="620" height="290" src="https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%201/4ink.jpg"><br>
</p>

here,
* m = 3
* J = 4
* N = 5
* fi = 1, for all the joints as they are of revolute type(refer table)

The DOF of this robot is calculated according to Grubler's forumala as = 3(5-1-4) + 4 = 4.
Thus, the DOF of the above robot is four.


## Querying robot Info and configuration in PyBullet

Here are some important functions which are used in getting the details of a robot.The necessary content for this subpart is listed below and the links lead to the exact page in the documentation.These functions are fairly straight forward and no more justice can be done to it rather than the documentation iteself !!.
* **Wait a few seconds after you open the link, it will take you to the exact location of the function.**
<div align="center">

[Base, Joint, Links](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.e27vav9dy7v6)

[getnumJoints,getJointInfo](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.la294ocbo43o)
  

[getJointState, resetJointState](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.p3s2oveabizm)

[getLinkState](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.3v8gjd1epcrt)
 
[getBaseVelocity](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.4vxw9j7piyjd)

</div>

## Task of the part:

_As a task of this part you are expected to do,_
<p align="center">
 <img  width="245" height="200" src="https://media1.giphy.com/media/GBNDuPWdIyPcY/source.gif"><br>
</p>

Make sure you go thorugh all these functions as they are clubbed with task for the next sub part.

_Its cloudy with a chance of quiz-fall though !!!_.Be prepared for the sudden shower of questions based on the theory anytime.
