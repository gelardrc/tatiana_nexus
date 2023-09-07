#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist,Vector3
import time

class nexus(object) : 
    
    def __init__(self):
        
        self.envia_comando = rospy.Publisher('cmd_vel',Twist,queue_size=10)

        pass

    def movimenta(self,mov):
        
        self.envia_comando.publish(mov)
        
        pass


def action():

    robot = nexus()

    #mov = Twist()

    velocidade = Twist(Vector3(1,0,0),Vector3(0,0,0))
    

    while not rospy.is_shutdown():

        robot.movimenta(mov=velocidade)

        time.sleep(1)

        pass


    pass


if __name__=='__main__':
    rospy.init_node('frente',anonymous=False)
    action()
