# ROS1 Workspace Organisation

Created: July 18, 2023 9:27 AM
Reviewed: No

Every ROS program resides in its package. Every package resides in the ROS workspace also named as the catkin_ws in general. 

```markdown
- catkin_ws/          # The root of your ROS workspace
  - build/                 # Directory for storing build files (auto-generated)
  - devel/                 # Directory for storing setup files (auto-generated)
  - src/                   # Directory for your ROS packages
    - package_1/           # Package 1 folder
      - CMakeLists.txt     # CMake build configuration for Package 1
      - package.xml        # Package manifest for Package 1
      - src/               # Source files for Package 1
      - include/           # Header files for Package 1 (optional)
      - launch/            # Launch files for Package 1 (optional)
      - config/            # Configuration files for Package 1 (optional)
      - ...
    - package_2/           # Package 2 folder
      - CMakeLists.txt     # CMake build configuration for Package 2
      - package.xml        # Package manifest for Package 2
      - src/               # Source files for Package 2
      - include/           # Header files for Package 2 (optional)
      - launch/            # Launch files for Package 2 (optional)
      - config/            # Configuration files for Package 2 (optional)
      - ...
    - ...
```

Notes on the workspace folder:

1. the catkin_ws can reside inside the home directory of the ubuntu system and should be created with the src directory inside it using the command
    
    ```bash
    cd ~
    mkdir -p ~/catkin_ws/src
    ```
    
2. catkin_ws can be replaced by any workspace_name as long as the folder structure is preserved
3. build and devel folders are autocreated as soon as you run the catkin init and catkin build command is executed, and the thus created build and devel folders should not be changed.
    
    ```bash
    cd ~/catkin_ws
    catkin init
    catkin build
    ```
    
4. the src folder contains all the sourcecode!