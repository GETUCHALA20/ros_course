#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from random import randint
def talker():
	pub = rospy.Publisher('chatter', Int32, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(1) # 10hz
	while not rospy.is_shutdown():
	        random_no = randint(1,100)
		rospy.loginfo(random_no)
		pub.publish(random_no)
		rate.sleep()

if __name__ == '__main__':
	try:
        	talker()
 	except rospy.ROSInterruptException:
		pass
