#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    node_name = 'hello_say'
    rospy.init_node(node_name)
    rospy.loginfo(f"Node ({node_name}) Started...")

    pub = rospy.Publisher('/altair/speech', String, queue_size=10)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(String(data=f"Hello World! {rospy.get_time()}"))
        rate.sleep()