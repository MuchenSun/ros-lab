# ROS TurtleBot3 VNC Docker Image
This docker image is built for turtlebot3 developers. It's based on another docker image "[dorowu/ubuntu-desktop-lxde-vnc](https://github.com/fcwu/docker-ubuntu-vnc-desktop)", which provides HTML5 VNC interface to access Ubuntu 16.04 LXDE desktop environment.

![launch test](./image/turtlebot3.jpg)

## Quick Start (only for Linux/MacOS users)
Clone the repository, then execute:

~~~
cd ros_turtlebot3_vnc/
chmod 755 launch.sh
./launch.sh
~~~

## Installation
### Method 1: Pull from [Docker Hub](https://hub.docker.com/r/muchensun/ros_turtlebot3_vnc/)
You can pull the image down by executing:

~~~
docker pull muchensun/ros_turtlebot3_vnc:v0.0
~~~

### Method 2: Built image from local Dockerfile 
First, clone this repository:

~~~
git clone https://github.com/MuchenSun/ros_turtlebot3_vnc.git
~~~

Then built the image by executing:

~~~
cd ros_turtlebot3_vnc
docker build -t ros_turtlebot3_vnc:v0.0 .
~~~

## Run the container
You can start a container by:

~~~
docker run -e RESOLUTION=1280x800 -p 6080:80 muchensun/ros_turtlebot3_vnc:v0.0
~~~

Then browse [http://127.0.0.1:6080/](http://127.0.0.1:6080/)

## Test
In the browser, open a terminal, then execute:

~~~
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_house.launch
~~~

You should see the following (first time launching might be slow)

![launch test](./image/gazebo.jpg)

*network connection is required to load the robot model*

## Reference
* This work is finished in [Distributed & Embedded System Lab](http://dslab.lzu.edu.cn/), Lanzhou University.
* [ROS Official Tutorial](http://wiki.ros.org/action/fullsearch/ROS/Tutorials?action=fullsearch&context=180&value=linkto%3A%22ROS%2FTutorials%22#ROS_Tutorials)
* [TurtleBot3 Official Manual](http://emanual.robotis.com/docs/en/platform/turtlebot3/)
* [A very helpful ROS course held ETH](http://www.rsl.ethz.ch/education-students/lectures/ros.html)
