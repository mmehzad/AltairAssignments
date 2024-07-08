#!/usr/bin/env python3

import rospy 
from sensor_msgs.msg import Image
import cv2
import cv_bridge

node_name = 'image_publish'

video_uri = 0  # this variable is the link to the video (default 0 is the webcam)
cap = cv2.VideoCapture(video_uri)
print(cap.isOpened())  # logging wont work here, as the node hasn't been initialized
bridge = cv_bridge.CvBridge()

if __name__ == '__main__':
    try:
        rospy.init_node(node_name)
        pub = rospy.Publisher('/video', Image, queue_size=1)

        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            ret, frame = cap.read()
            rospy.loginfo(f"PUBLISHING")
            if not ret:
                break

            msg = bridge.cv2_to_imgmsg(frame, 'bgr8')
            pub.publish(msg)
            rate.sleep()

        cap.release()

    except rospy.ROSInterruptException:
        cap.release()