from setuptools import setup, find_packages

VERSION = '0.0.0'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'ros-lab',
    version = VERSION,
    author = 'Muchen Sun',
    author_email = 'sunmch15@foxmail.com',

    description = 'Docker-Based Robot Operating System Virtual Lab',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/MuchenSun/ros-lab',
    
    packages = find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires = [
        'docker >= 3.4.0'
    ],

    keywords = 'ROS Docker',

    license = 'GPLv3',

    entry_points = {
        'console_scripts':[
            'ros-lab = ros_lab.entry:main'
        ]
    }
)