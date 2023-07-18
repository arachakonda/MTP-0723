#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(msg):
  print(msg.data)

def listener():
    rospy.init_node('topic_subscriber')
    rospy.Subscriber('/message_topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()