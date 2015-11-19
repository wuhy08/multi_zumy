#!/usr/bin/env python
import tf
import rospy
import sys
import math
import numpy as np
from geometry_msgs.msg import Twist


#REFERENCE FOLLOW_AR_TAG_MANUAL IN LAB 6

def MultiZumy(zumy1, zumy2):
    
    #Allow node to publish to topic
    zumy_vel1 = rospy.Publisher('/%s/cmd_vel' % zumy1, Twist, queue_size=2)
    zumy_vel2 = rospy.Publisher('/%s/cmd_vel' % zumy2, Twist, queue_size=2)
    
    #Set Rate
    rate = rospy.Rate(10)

    #Create moving twist
    cmd = Twist()
    cmd.linear.x = .2
    cmd.linear.y = 0
    cmd.linear.z = 0
    cmd.angular.x = 0
    cmd.angular.y = 0
    cmd.angular.z = 0
    
    
    #Publish moving twist to topic
    time = 50
    while time > 0:    
        zumy_vel1.publish(cmd)
        zumy_vel2.publish(cmd)
        rate.sleep()
        time = time - 1
        print('Countdown to Stop: %d' % time)
    
    #Create killing twist 
    cmd.linear.x = 0
    cmd.linear.y = 0
    cmd.linear.z = 0
    cmd.angular.x = 0
    cmd.angular.y = 0
    cmd.angular.z = 0
    
	#Publish killing twist to topic
    zumy_vel1.publish(cmd)
    zumy_vel2.publish(cmd)
    print 'Finished!'
    
if __name__=='__main__':
    
    #Makes sure the correct number of input arguments exist
    if len(sys.argv) < 3:
        print('Wrong Number of Arguments!  Use: MultiZumy.py [ zumy1 name ] [ zumy2 name ]')
        sys.exit()

    #Initiates the zumyxy node
    rospy.init_node('MultiZumy')
    
    #Runs the code
    MultiZumy(sys.argv[1], sys.argv[2])
    rospy.spin()

