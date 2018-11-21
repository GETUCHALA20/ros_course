#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
def callback(data):
	square_value = data.data * data.data
	rospy.loginfo(rospy.get_caller_id() + "The square root of %f is %f",data.data , square_value)     
def listener():

	# In ROS, nodes are uniquely named. If two nodes with the same
        # node are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node('listener', anonymous=True)
   
        rospy.Subscriber("chatter", Int32, callback)
   
        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()
 
if __name__ == '__main__':
	listener()
