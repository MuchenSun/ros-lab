# ROS-Lab: Docker-Based Robot Operating System Virtual Lab
A Docker-based virtual lab of Robot Operating System to help beginners learn and practise. It's based on docker image "muchensun/ros_turtlebot3_vnc", which is built on another docker image ["dorowu/ubuntu-desktop-lxde-vnc"](https://github.com/fcwu/docker-ubuntu-vnc-desktop). This lab is wrapped by a command line tool to simplify operations.

![launch test](https://raw.githubusercontent.com/MuchenSun/ros-lab/master/image/turtlebot3.jpg)

## Installation
*It's highly recommended to create a conda Python3 environment before installation.*

You can use [`pip`](https://pip.pypa.io/en/stable/installing/) to install(remember to use Python3), type the following command:

~~~
pip install ros-lab
~~~

## How to use
1. Type `ros-lab` in command line, you will enter ros-lab.
2. Input `help` or `?` for command information.
3. Have fun with ros-lab !

![launch test](https://raw.githubusercontent.com/MuchenSun/ros-lab/master/image/gazebo.jpg)

## Several tips
1. For Ubuntu users, you may need to configure Docker before you start. If you have problems about user permission, please try the first answer [here](https://superuser.com/questions/835696/how-solve-permission-problems-for-docker-in-ubuntu). 
2. After executing the "start_lab" command, it may take some time to start the lab. You can try to refresh the page.
3. For current version dosen't support stopping and saving the container(forgive me, I will add it as soon as I can), if you have problem when restarting the lab, it might be helpful to restart Docker or stop all running containers. But remember it will recover the state of the container.

## Useful links
* This work is finished in [Distributed & Embedded System Lab](http://dslab.lzu.edu.cn/), Lanzhou University.
* ROS [Official Tutorial](http://wiki.ros.org/action/fullsearch/ROS/Tutorials?action=fullsearch&context=180&value=linkto%3A%22ROS%2FTutorials%22#ROS_Tutorials).
* TurtleBot3 [Official Manual](http://emanual.robotis.com/docs/en/platform/turtlebot3/).
* A very helpful [ROS course](http://www.rsl.ethz.ch/education-students/lectures/ros.html) held by ETH.
