#! /usr/bin/env python3
import rospy
from std_msgs.msg import String 

rospy.init_node('topic_publisher') #node name
pub = rospy.Publisher('/message_topic', String, queue_size=1)
rate = rospy.Rate(2)
message = String()
message.data = "Hello World!"

while not rospy.is_shutdown(): 
  pub.publish(message)
  rate.sleep()