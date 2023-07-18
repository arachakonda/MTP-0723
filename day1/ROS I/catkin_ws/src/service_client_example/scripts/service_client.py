#! /usr/bin/env python3

import rospy
# Import the service message used by the service /service_example
from service_server_example.srv import pickVar, pickVarRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client_node')
# Wait for the service client /service_example to be running
rospy.wait_for_service('/service_server')
# Create the connection to the service
val_by_name_service = rospy.ServiceProxy('/service_server', pickVar)
# Create an object of type getCurrentTimeRequest
traj_by_name_object = pickVarRequest()
# Fill the variable var_name of this object with the desired value
traj_by_name_object.var = "b"
# Send through the connection the name of the trajectory to be executed by the robot
result = val_by_name_service(traj_by_name_object)
# Print the result given by the service called
print(result)