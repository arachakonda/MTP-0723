# Publisher

Created: February 16, 2023 10:12 PM
Class: ROS1PY BASICS
Type: Reading
Reviewed: No

Navigate to the scripts folder of the created package using the following commands:

```bash
cd ~/catkin_ws/src/publisher_example
mkdir scripts
```

navigate into the scripts folder and create the publisher script:

```bash
cd scripts
touch publish_via_topic.py
```

note that though this script is create it is not yet executable. and to do this you can use the command:

```bash
chmod +x publish_via_topic.py
```

open the publish_via_topic.py with the following editor:

```python
#! /usr/bin/env python

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
```

The code above creates a ROS publisher script that publishes a "Hello World!" message to the `/message_topic` topic at a rate of 2 Hz. Make sure to save the file once you have copied the code.