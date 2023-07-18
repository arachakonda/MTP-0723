# Custom Messages

Created: July 18, 2023 10:49 PM
Class: ROS1PY BASICS
Type: Reading
Reviewed: No

custom messages can be created to facilitate transfer of heterogenous ROS datatypes together in a single message.

The custom message creation process is in 4 steps:

- navigate to the ros package and create custom message directory

```bash
roscd publisher_example
mkdir msg
```

- navigate to the msg folder and create the custom

message file using the .msg extension

```bash
cd msg
touch custom.msg
```

- define the structure of the custom message using the appropriate ROS native data types

The following are ROS native data types that can be used when defining the structure of a custom message:

- `int8`, `int16`, `int32`, `int64`
- `uint8`, `uint16`, `uint32`, `uint64`
- `float32`, `float64`
- `string`
- `time`
- `duration`
- `bool`
- Arrays and nested arrays of the above data types

```
int32 id
string name
float32 score
```

- To edit the `CMakeLists.txt` file for the custom message, follow these steps:
    1. Open the `CMakeLists.txt` file located in the root of your ROS package.
    2. **Add** the `message_generation` dependency to the `find_package` section of the `CMakeLists.txt` file:
        
        ```
        find_package(catkin REQUIRED COMPONENTS
          roscpp
          rospy
          std_msgs
          message_generation
        )
        ```
        
    3. **Add** the following line to the file to ensure that the message files are generated during the build process:
        
        ```
        add_message_files(
          FILES
          custom.msg
        )
        
        ```
        
    4. Add the following line to the `generate_messages` section of the `CMakeLists.txt` file if you plan to use the custom message in your ROS node:
        
        ```
        generate_messages(DEPENDENCIES std_msgs)
        ```
        
    5. **Add** the `message_runtime` dependency to the `catkin_package` section of the `CMakeLists.txt` file:
        
        ```
        catkin_package(
          CATKIN_DEPENDS message_runtime #add this, this may not be the only dep
        )
        ```
        
    6. Save the `CMakeLists.txt` file and run `catkin_make` to rebuild your ROS package with the custom message.
- Here is an example `package.xml` for a package that includes a custom message called `CustomMessage`:
    
    ```xml
    <?xml version="1.0"?>
    <package format="2">
      <name>publisher_example</name>
      <version>0.0.1</version>
      <description>My ROS package</description>
      <maintainer email="me@example.com">My Name</maintainer>
      <license>MIT</license>
    
      <buildtool_depend>catkin</buildtool_depend>
      <build_depend>roscpp</build_depend>
      <build_depend>rospy</build_depend>
      <build_depend>std_msgs</build_depend>
      <build_depend>message_generation</build_depend>
      <exec_depend>roscpp</exec_depend>
      <exec_depend>rospy</exec_depend>
      <exec_depend>std_msgs</exec_depend>
      <exec_depend>message_runtime</exec_depend>
    
    </package>
    
    ```
    
- build the ROS messages using catkin build and source the workspace to recognise generated messages

```bash
roscd; cd ..
catkin build
source devel/setup.bash
```