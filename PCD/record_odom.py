#!/usr/bin/env python
#coding=utf-8

import numpy 
import rospy
from nav_msgs.msg import Odometry #使用时需要修改数据类型PoseWithCovarianceStamped

list_TF = []
def get_info (msg):
    trans = []
    trans.append(msg.header.stamp.to_sec()) #time
    trans.append(msg.pose.pose.position.x)
    trans.append(msg.pose.pose.position.y)
    trans.append(msg.pose.pose.position.z)
    rot = [0, 0, 0, 1]
    #rot.append(msg.pose.pose.orientation.x)
    #rot.append(msg.pose.pose.orientation.y)
    #rot.append(msg.pose.pose.orientation.z)
    #rot.append(msg.pose.pose.orientation.w)
    TF = trans + rot
    list_TF.append(TF)
    numpy.savetxt('Trajectory_noAttitude.txt',list_TF, fmt='%s')
    print(TF)
 
rospy.init_node('record_odom')
list_log = []
list_log_yaw = []
sub = rospy.Subscriber ('/Odometry', Odometry, get_info, queue_size=1000)
 
r = rospy.Rate(50)
while not rospy.is_shutdown():
    r.sleep()
