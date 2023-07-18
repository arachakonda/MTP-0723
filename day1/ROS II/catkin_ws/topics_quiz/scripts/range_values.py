#! /usr/bin/env python3
import csv
import rospy
from sensor_msgs.msg import LaserScan


def callback(scan_data: LaserScan):
    left_distance = scan_data.ranges[0]
    center_distance = scan_data.ranges[333]
    right_distance = scan_data.ranges[719]
    with open('ranges.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([str(left_distance), str(
            center_distance), str(right_distance)])
    print("left: %f, center: %f, right: %f" % (left_distance,
          center_distance, right_distance))


if __name__ == '__main__':
    rospy.init_node('topics_quiz_node_vals')
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()
