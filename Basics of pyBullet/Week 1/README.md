# Week 1
The first week of the camp covers the following topics, evenly distributed into three subparts folders.
## The topics are:

* Introduction to simulations and need for simulation.
* Intro to Pybullet, why PyBullet over other simulators?.
* Installation of PyBullet.
* Intro to urdf files, robot geometry, links, base, joints.
* Demonstrating some examples of PyBullet simulations.
* Basic functions in PyBullet: connect, gravity, loading urdf, saving,
creating shapes, simulation, positions, and orientations in PyBullet.

## FAQ:
1. Error: Microsoft Visual C++ 14.0 is required while installation of Pybullet:</br>
   * Refer to this [link](https://docs.microsoft.com/en-us/answers/questions/136595/error-microsoft-visual-c-140-or-greater-is-require.html). Answer given here works perfectly.
2. How to fix cannot load URDF errors?
   * Make sure your have given the correct path to the URDF file in the p.loadURDF function.
   * Also make sure you haven't altered any tags in the URDF file, try to recheck with the original urdf file given. You can also use [this](https://mymodelrobot.appspot.com/5629499534213120) website for checking your URDF file.
