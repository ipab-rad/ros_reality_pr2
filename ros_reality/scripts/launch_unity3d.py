#!/usr/bin/env python
import os
import sys
import rospy

rospy.init_node('unity3d', anonymous=False)
unity_path = rospy.get_param("~unity_path", default="unity3d")
ros_reality_path = rospy.get_param("~ros_reality_path", default="path")

os.system(unity_path + " -projectPath " + ros_reality_path)

