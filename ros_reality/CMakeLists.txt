cmake_minimum_required(VERSION 2.8.3)
project(ros_reality_pr2)

find_package(catkin REQUIRED COMPONENTS
		rospy)

catkin_package(CATKIN_DEPENDS
		rospy
		ros_reality_bridge)
