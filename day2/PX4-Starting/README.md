# PX4-Starting

## Installations

### 1. QGroundControl

Install QgroundControl from here [QGroundControl](https://docs.qgroundcontrol.com/master/en/getting_started/download_and_install.html)

### 2. PX4 Autopilot

Install PX4 from [PX4](https://docs.px4.io/master/en/dev_setup/dev_env_linux_ubuntu.html#ros-gazebo)

Only install `Gazebo, JMAVSim and NuttX (Pixhawk) Targets`section of the above document

### 3. Mavlink and MAVROS in catkin workspace

Install these as here [ROS with MAVROS](https://docs.px4.io/master/en/ros/mavros_installation.html)

In this replace `kinetic` everywhere with `melodic` as a general rule.

Steps : 

- Please Install both via binary and source installations.
- In Binary Installation, execute both the steps. 
    - Install the first 3 steps as they are. Till `wstool init ~/catkin_ws/src`
    - In MAVROS : Only run the Released/stable command. **DO NOT** run Latest source.
    - Run the next 3,4,5,6 steps as they are.

Note : Please make sure the PX4_Autopilot is **NOT** cloned within catkin_ws. They can be in totally separate locations.

### 4. Launch :

Run these commands to launch [Gazebo_Launch](https://docs.px4.io/master/en/simulation/gazebo.html)

### Debug 1:

Once installed, in catkin_ws, in `~/catkin_ws/src/mavros/mavros/launch/px4_config.yaml`, change `use_quaternion:false` to `use_quaternion:true`

# To Run Custom Controller

### 1. Test Run

Before running the controller, it's always good to verify if every installation is working the way it is supposed to do. You do not have to run in every time. Just the very first time 🙂.

- Open a terminal :
    - cd into the PX4-Autopilot folder. `cd /path/to/PX4-Autopilot`
    - Run the following commands. These are for sourcing the necessary packages.
        - `source ~/catkin_ws/devel/setup.bash`
        - `source Tools/simulation/gazebo/setup_gazebo.bash $(pwd) $(pwd)/build/px4_sitl_default`
        - `export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)`
        - `export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)/Tools/sitl_gazebo`
    - Launch PX4 with the following command.
        
        `roslaunch px4 mavros_posix_sitl.launch`
        
        You should be a able to see a drone spawned. 
        
- Open the QgroundControl App :
    - You should see that it says : Ready to Fly in the top left corner. (Ref. Screenshot attached)
    - Click on Takeoff. It should prompt slide to take off in the bottom.
    - Once you slide it, you should see the drone taking off in gazebo
    - Zoom in to the map in QGC and click anywhere close to the take off point (It is the point that is shown by the RED arrow : Ref. Screenshot attached).
    - It will give an option go to point. Click on it. It should again prompt for a slider.
    - After you slide it, you should see the drone moving in gazebo. Note : Based on the point you chose, most likely the drone will far away in gazebo. Zoom out and try to find the drone.
    - You can use the return option on QGC to get the drone back to its starting point.
    - Try giving the drone different points(they are called waypoints) and see how the drone is moving if you want to. We would be doing the same during controller tuning but through a terminal (Instructions for this in the next section).

![QGC.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c920ad1f-fe13-4a01-9e05-c9fe0dd25b95/QGC.png)

### 2. Custom Controller

Assuming the Test Run is working well, these are the steps to run your controller on a drone.

Open 3 terminals:

- Terminal 1 :
    - cd into the PX4-Autopilot folder. `cd /path/to/PX4-Autopilot`
    - Run the following commands. These are for sourcing the necessary packages.
        - `source ~/catkin_ws/devel/setup.bash`
        - `source Tools/simulation/gazebo/setup_gazebo.bash $(pwd) $(pwd)/build/px4_sitl_default`
        - `export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)`
        - `export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)/Tools/sitl_gazebo`
    - Launch PX4 with the following command.
        
        `roslaunch px4 mavros_posix_sitl.launch`
        
        You should be a able to see a drone spawned. 
        
- Terminal 2 :
    - Clone this repo. This folder can be anywhere on you PC. `cd /path/to/scripts`
    - Sourcing: `source ~/catkin_ws/devel/setup.bash`
    - Run any python file you like within the folder. `python anyfile.py`.There are 4 files.
        - offboard_sub.py : This is basic file which will fly the drone in offboard mode. offboard is when the done is controlled by a drone rather than remote control.
        - PID_att.py : This is a basic PID controller. This is very stable.
    - The drone should hover at height of 1m after you run any python file.
- Terminal 3:
    - Sourcing: `source ~/catkin_ws/devel/setup.bash`
    - Run this command
        
        `rostopic pub /new_pose geometry_msgs/PoseStamped "header:
        seq: 0
        stamp:
        secs: 0
        nsecs: 0
        frame_id: ''
        pose:
        position:
        x: 0.5
        y: 0.0
        z: 2.0
        orientation:
        x: 0.0
        y: 0.0
        z: 0.0
        w: 0.0"`
        
        - You do have to type the entire thing. Type this : `rostopic pub /new_pose geometry_msgs/PoseStamped` and then hit TAB multiple times till you see the command as above. Change the x,y,z of the position to where ever you want your drone to go. Give values in small increments. Large increments will crash the drone. Especially if large increments are given in x and y direction.