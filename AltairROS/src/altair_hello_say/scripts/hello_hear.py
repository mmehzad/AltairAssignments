#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(f"Recieved: {data.data}")

if __name__ == '__main__':
    node_name = 'hello_hear'
    rospy.init_node(node_name)

    rospy.Subscriber('/altair/speech', String, callback)
    rospy.spin()