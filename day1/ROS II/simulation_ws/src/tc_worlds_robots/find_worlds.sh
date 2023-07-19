#! /bin/bash

# declare some vars
export LOOKAT="/home/simulations/public_sim_ws/src/all"
export CREATEAT="${LOOKAT}/tc_worlds_robots/launch"
export WORLDS=$(find $LOOKAT -type f -name *.world)
export WORLDS_COUNT=$(find $LOOKAT -type f -name *.world | xargs -0 | wc -l)

# create report file
export report_file=report.txt
touch $report_file
echo "" > $report_file

# start iteration
n=0
echo "Total of ${WORLDS_COUNT} world files"
for fullpath_file in $WORLDS
do
  # count iterations
  ((n++))
  echo "${n} of ${WORLDS_COUNT}"

  # get parameters
  filename=$(basename $fullpath_file)
  filename_only="${filename%.*}"
  extension="${filename##*.}"

  # create file
  content=$(cat <<EOF
<?xml version="1.0"?>
<launch>
  <arg name="debug" default="false"/>
  <arg name="gui" default="false"/>
  <arg name="pause" default="false"/>
  <arg name="headless" default="false"/>

  <include file="\$(find gazebo_ros)/launch/empty_world.launch">
    <arg name="world_name" value="$fullpath_file"/>
    <arg name="debug" value="\$(arg debug)" />
    <arg name="gui" value="\$(arg gui)" />
    <arg name="paused" value="\$(arg pause)"/>
    <arg name="use_sim_time" value="true"/>
    <arg name="headless" value="\$(arg headless)"/>
  </include>
</launch>
EOF
)
  # create launch file
  export launch_file=$CREATEAT/world_$filename_only.launch
  touch $launch_file
  echo "${content}" > $launch_file

  # fill report file
  echo $fullpath_file >> $report_file
  echo $filename >> $report_file
  echo $launch_file >> $report_file
  echo "" >> $report_file
done
