#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
import cv2
import cv_bridge

node_name = 'image_subscribe'
rospy.init_node(node_name)

def callback(msg):
    rospy.loginfo(msg)
    bridge = cv_bridge.CvBridge()
    cv2.imshow('video', bridge.imgmsg_to_cv2(msg))
    cv2.waitKey(1)


if __name__ == '__main__':
    rospy.Subscriber('/video', Image, callback)
    rospy.spin()

    cv2.destroyAllWindows()