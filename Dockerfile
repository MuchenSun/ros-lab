FROM dorowu/ubuntu-desktop-lxde-vnc:xenial

RUN echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list \
    && /bin/bash -c 'apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 0xB01FA116 \
    && apt-get update \
    && apt-get -y install ros-kinetic-desktop-full \
    && rosdep init \
    && rosdep update \
    && apt-get -y install python-rosinstall'

RUN /bin/bash -c 'apt-get -y install ros-kinetic-joy \
                                        ros-kinetic-teleop-twist-joy \
                                        ros-kinetic-teleop-twist-keyboard \
                                        ros-kinetic-laser-proc \
                                        ros-kinetic-rgbd-launch \
                                        ros-kinetic-depthimage-to-laserscan \
                                        ros-kinetic-rosserial-arduino \
                                        ros-kinetic-rosserial-python \
                                        ros-kinetic-rosserial-server \
                                        ros-kinetic-rosserial-client \
                                        ros-kinetic-rosserial-msgs \
                                        ros-kinetic-amcl \
                                        ros-kinetic-map-server \
                                        ros-kinetic-move-base \
                                        ros-kinetic-urdf \
                                        ros-kinetic-xacro \
                                        ros-kinetic-compressed-image-transport \
                                        ros-kinetic-rqt-image-view \
                                        ros-kinetic-gmapping \
                                        ros-kinetic-navigation \
                                        ros-kinetic-interactive-markers \
    && mkdir -p /root/catkin_ws/src \
    && cd /root/catkin_ws/src/ \
    && git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git \
    && git clone https://github.com/ROBOTIS-GIT/turtlebot3.git \
    && git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git \
    && cd /root/catkin_ws \
    && source /opt/ros/kinetic/setup.bash \
    && source /root/.bashrc \
    && catkin_make \
    && echo "source /opt/ros/kinetic/setup.bash" >> /root/.bashrc \
    && echo "source /root/catkin_ws/devel/setup.bash" >> /root/.bashrc \
    && source /root/.bashrc \
    && apt-get -y install wget vim terminator\
    && wget -O /root/.vimrc https://raw.githubusercontent.com/amix/vimrc/master/vimrcs/basic.vim'
