#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_circle(ref_counter):
    msg = Twist()
    msg.linear.x = 2
    msg.angular.z = 1

    pub.publish(msg)
    rate.sleep()

def move_spiral(ref_counter):
    msg = Twist()
    msg.linear.x = 2
    msg.angular.z = 5*((1 - 0.1)**ref_counter)

    pub.publish(msg)
    rate.sleep()

def move_square(ref_counter):
    msg = Twist()
    msg.linear.x = 10
    pub.publish(msg)
    rate.sleep()

    msg.linear.x = 0
    msg.linear.y = 10
    pub.publish(msg)
    rate.sleep()

    msg.linear.y = 0
    msg.linear.x = -10
    pub.publish(msg)
    rate.sleep()

    msg.linear.x = 0
    msg.linear.y = -10
    pub.publish(msg)
    rate.sleep()



if __name__ == '__main__':
    node_name = 'altair_control'
    rospy.init_node(node_name)
    rospy.loginfo(f"Node ({node_name}) Started...")

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(2)

    move_cmd = input()
    logics = {
        'A': move_circle,
        'B': move_square,
        'C': move_spiral,
    }

    ref_counter = 0
    while not rospy.is_shutdown():
        logics.get(move_cmd, 'A')(ref_counter)
        rospy.loginfo(f"COUNTER: {ref_counter}")
        ref_counter += 1