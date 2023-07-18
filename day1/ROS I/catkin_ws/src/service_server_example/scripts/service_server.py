#! /usr/bin/env python3
import rospy
from service_server_example.srv import pickVar, pickVarResponse

a = 2
b = 3

def handle_pickVar(req):
    print("Returning [var = %s]"%(req.var))
    if req.var == "a":
        return pickVarResponse(a)
    elif req.var == "b":
        return pickVarResponse(b)

def picVar_server():
    rospy.init_node('service_server_node')
    s = rospy.Service('service_server', pickVar, handle_pickVar)
    print("Ready to return var.")
    rospy.spin()

if __name__ == "__main__":
    picVar_server()