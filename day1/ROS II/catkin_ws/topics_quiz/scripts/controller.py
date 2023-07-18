#! /usr/bin/env python3
import csv
import math
import rospy
from geometry_msgs.msg import Twist


if __name__ == "__main__":
    inp = Twist()
    rospy.init_node('topics_quiz_node')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        print('----pub triggered----')
        with open('ranges.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                l = float(row[0])
                c = float(row[1])
                r = float(row[2])

        if (c > 0.5) and not(math.isinf(c)):
            inp.linear.x = 0.05
            if r > 0.3:  # farther from the wall? turn towards
                inp.angular.z = -0.2
            elif r < 0.2:  # closer to the wall? turn away
                inp.angular.z = 0.2
            elif r == 0.3:
                inp.angular.z = 0
        else:
            if c <= 0.3:
                inp.linear.x = -0.1
            if c > 0.3:
                inp.linear.x = 0.05
                inp.angular.z = 0.5
        pub.publish(inp)
        rate.sleep()
