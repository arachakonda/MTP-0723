# Topics

Created: February 16, 2023 10:12 PM
Class: ROS1PY BASICS
Type: Reading
Reviewed: No

Topics are essentially pipes that are defined to carry specific kind of data / messages.

refer to the topics slides for more details on their internal funtioning.

rostopic is the command used to access all the functions available under the ROS topic from the shell

```bash
rostopic list
```

is used to list all available ROS topics

```bash
rostopic info <topic_name>
```

is used to list all available topic names

```bash
rostopic echo <topic_name> -n1
```

is used to print one chunk/ stream of data being published on the ROS topic

```bash
rostopic pub <topic_name> <message_type> message
```

is used to publish one chunk of data on the ROS topic using the publish command