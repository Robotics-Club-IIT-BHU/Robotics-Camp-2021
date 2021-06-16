# Subpart 2
<p align="center">
   <img  width="300" height="400" src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTNj2q4taXWApBMAdeOBpYTV6bgscqqyECt-DRMTeC2zuKN0QcC&usqp=CAU">
</p>


Well, given that we have played enough with individual structures and functions, its time to get into the paradigm of kinematics to address the motion needs of our Robots in a more structure way. So, the definition of kinematics goes like this:

_**" the branch of mechanics concerned with the motion of objects without reference to the forces which cause the motion"**_.
for most of us, the earliest remembrance of kinematics would have been the figure below

<p align="center">
   <img  width="730" height="390" src="https://thumbs.gfycat.com/YearlySnivelingAlligatorsnappingturtle-small.gif">
</p>

## Well, are we still gonna deal with y = (tan θ)x – gx^2/2(vcosθ)^2?

_Ans: Dw, Not the case any more !!_

But now we kick things up a little and redefine things for the exclusive case of robotics. One of the major differences in robotics is the fact that we are mostly expected to work with **articulated systems**, in simple terms the body of interest is generally made up of *multiple links/sub-bodies*. From the previous parts, you might be familiar with this idea, but we still hold on to the fundamental definition of Kinematics and our formulation revolves around only with the **motion of such bodies** and not its cause. Though this might sound simple, it is not quite so as we expect any form of motion of the robot to be caused by the motors that are local to the robot. But on a higher level of abstraction, this is still a good approach attacking the robot motion problem.

## The Kinematics Problem we are interested in:
 So, by Kinematics what we mean is a way to transform from the **robot space system** to the **world space system** and vice versa. Meaning we are in search of ways to find which orientation of specific links can allow the endpoint of a given chain of links/arm to reach a given point in the **3D cartesian space**.

**Note:** The End point of a given chain of links, is gernarally called as **end effector** of that arm.The point marked as _**E**_, in the picture below is the end effector of a 2R planar robot.
<p align="center">
   <img  width="400" height="280" src="https://robotacademy.net.au/wp-content/uploads/2017/03/6.3-Checkunderstanding-Q3.png">
</p>

Eg:

Take the case of a 2R robot kept on a xy plane. that you built in **Part-1**. Now let us say the end of the arm needs to reach a point (1,1,0) in 3D space(as the robot is planar but the simulation is 3d), how would you go about solving this problem?

Logically, the questions you should ask will be,

1. Whether such a configuration of the robot is possible in the first place ?(given the length of links,a1 and a2 in the figure above, joint angle limits, etc)

2. If yes, what should be the individual angles required to be kept at the two joints of the arm.(q1 and q2 in the figure above)

This also gives rise to the problem that is the inverse in nature. Hence, in a nutshell, we broadly classify these two problems as two types of kinematics for a given robot namely,

1. _Given a value for each joint angles where will my end effector be? - answered by **Forward Kinematics**_
2. _Given a value, the end effector target position, what will by corresponding joint angles be to reach such a configuration? - answered by **Inverse Kinematics**_

## Forward Kinematics:

<div align="center">

_Fk - The Destination Finder_

_I know to take left, right, left, where will I reach ?_

</div>

The forward kinematics of a robot refers to the calculation of the position and orientation of its end-effector frame from its joint coordinates θ . The link lengths are a1, a2 as in the 2r robot above. Choose a fixed frame, with the origin located at the base joint as shown, and assume an end-effector frame E has been attached to the tip of the second link. The Cartesian position (x, y) and orientation end-effector frame as functions of the joint angles (q1,q2 ) are then calculated in the forward kinematics.

**Note:** 

_Why, do we need IK in the first place then?_
.
<p align="center">
   <img  width="400" height="280" src="https://img.memecdn.com/cat-robotics-gone-bad_o_7097823.jpg">
</p>


_Well, at times you have data about the angles to follow and at times about the trajectory and will be using FK and IK respectively. We thus need IK in the case of control._

## Inverse Kinematics:

<div align="center">
   
_Ik - The Path Finder_

_I know the goal point, figure out the path !!_

</div>

For a general n degree-of-freedom open chain with forward kinematics θ ∈ R n , the inverse kinematics problem can be stated as follows: given a point in world space, find solutions θi for all i in num of joint, where θi is the angle of the ith joint, that satisfies the end-effector position.

That's, the so-called definition of both and from my perspective during my first exposure, *Forward Kinematics* looked fairly straight forward and *Inverse Kinematics* looked like some form of black magic. So, if you are already able to imagine just the outlying structure and definition of the problem just by it definition,..kudos !!.If not, the video below explains the analytical formulation of IK and FK for a 2R planar robot,as nothing can make it clearer than equations.

**Analytical Solution:** [Robotics - Direct and Inverse Kinematics of 2 DoF planar robot](https://www.youtube.com/watch?v=Ad5DLd8vrbQ)


**Note:** 

At this point, I am obliged to inform all the readers that we are aware of **the complications in higher dimensional robots, DH parameters, Transformation and Rotation Matrix-based approaches and other sophisticated formulations** but this camp is motivated towards giving you an head start with all the wholesome fundamental concepts.So,it is essentially out of the scope of this course but we are ready to share material upon an individual's interest.**All the task will be limited to planar/2D robots as discussed in the Analytic solution video** 

## Additional Video resources:

1. Coding Challenge - by Daniel Shiffman, is a serious of computer programming challenges generally in JAVA based platforms.

    1. [Forward Kinematics](https://www.youtube.com/watch?v=xXjRlEr7AGk)
    2. [Inverse Kinematics](https://www.youtube.com/watch?v=hbgDqyy8bIw)

**Note:** In the above videos, **just refer to his explanation and approach he takes for implementing a IK and FK for an n-link 2D planar chain**, while it is not required to take his exact approach or try programing in **processing** like him.


2. [FK vs IK , an animation based explanation](https://www.youtube.com/watch?v=0a9qIj7kwiA)

3. [Hardware implementation of IK an FK on a 2R robot](https://www.youtube.com/watch?v=3rFaZMvgNe8)

## Task for the part:

**Task 1:**

1. Implement functions implementing Forward Kinematics and Inverse Kinematics for a planar 2R planar robot, with link lengths l1,l2.
 
 2. Use the above functions to make the 2R robot in [2R_planar_robot.urdf](2R_planar_robot.urdf) follow the **longest straight-line segment the robot could follow with the given link lengths l1,l2** by making l1 and l2 equal to the lengths in the urdf. Refer the starter code for more details.[ik_starter.py](ik_starter.py)
 
Like,in the visualization below you can make your robot trace anything, your creativity is your limit !!, but we expect only following a **line segment though.**

<p align="center">
   <img  width="330" height="325" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/SCARA_right.gif/330px-SCARA_right.gif">
</p>

**Note:** 

1. You are expected to find the **longest line segment, this robot can trace) and update the end points and equation of the straight line in the code**.

2. Along with the code,**just share a gif/screenshot of the robot tracing a straight line in the solution along with the code**.

3. You are **strictly prohibited** to use the inbuilt *calculateInverseKinematics* function but implement your own ik function for Task 1 whereas you are expected to use it in Task 1.5.


Before moving on to the next task,It can get fairly complicated for building a IK function from scratch at times.So,Pybullet has a inbuilt function for solving the Inverse Kinematics for a given robot urdf.As, the saying goes...*for enlightenment ,read the bible !!!*

<div align = "center">
   
   [calculateInverseKinematics](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.9i02ojf4k3ve)

</div>

**Task 1.5:**

Well, you guessed it right !!

Use the inbuilt function to make the **end effector** follow the line segment for the 2R planar robot.
