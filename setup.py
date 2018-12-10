#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages

VERSION = '0.3'

# with open("README.md", "r") as fh:
#     long_description = fh.read()
long_description = 'A Docker-based virtual lab of Robot Operating System to help beginners learn and practise. It\'s based on docker image "muchensun/ros_turtlebot3_vnc", which is based on docker image "dorowu/ubuntu-desktop-lxde-vnc", and wrapped by a read-eval-print loop(REPL) interface implemented with Python.'

setup(
    name='ros-lab',
    version=VERSION,
    author='Muchen Sun',
    author_email='sunmch15@foxmail.com',

    description="Docker-Based Virtual ROS Lab for Beginners",
    long_description=long_description,
    # long_description_content_type="text/markdown",
    url='https://github.com/muchensun/ros-lab',

    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'docker >= 3.0.0',
    ],

    keywords='python ROS Docker',

    license='Apache',

    entry_points={
        'console_scripts':[
            'ros-lab = lab.main:lab'
        ]
    },
)
