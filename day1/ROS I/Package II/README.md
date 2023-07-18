# Package II

Created: July 18, 2023 12:03 PM
Class: ROS1PY BASICS
Type: Reading
Reviewed: No

Each created package contains a package.xml file. catkin is the buildtool dependency which is present by default

```xml
<build_depend>rospy</build_depend>
<build_depend>roscpp</build_depend><!--This is optional for a pythonic example-->
<build_depend>std_msgs</build_depend>

<exec_depend>rospy</exec_depend>
<exec_depend>roscpp</exec_depend>
<exec_depend>std_msgs</exec_depend>
```

The above lines of code specify the build and execution dependencies for the package. In this case, the package depends on the rospy, roscpp, and std_msgs libraries. These dependencies build and run the package correctly. Additionally, the package.xml file provides important information about the package, such as its name, version, and description. This information is used by other packages and tools when working with the package.

Add the following lines to the `CMakeLists.txt` file instead of the previous code block for a python script:

```
cmake_minimum_required(VERSION 2.8.3)
project(package_name)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy std_msgs
)

catkin_install_python(PROGRAMS scripts/script_name.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

```

This code block sets up CMake to execute a Python script. It finds the necessary packages (rospy and std_msgs) using `find_package` and sets the `catkin_package` macro with the same dependencies. Instead of `add_executable`, we're using `catkin_install_python` to install the Python script into the package's binary directory. Replace `scripts/script_name.py` with the path to your Python script.