# -*- encoding: UTF-8 -*-

''' PoseZero: Set all the motors of the body to zero. '''

import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Zero
    #postureProxy.goToPosture("StandZero", 0.5)
    postureProxy.goToPosture("Stand", 0.5)

    # We use the "Body" name to signify the collection of all joints and actuators
    RShoulderPitch = "RShoulderPitch"
    LShoulderPitch = "LShoulderPitch"
    HeadPitch = "HeadPitch"
    HeadYaw = "HeadYaw"
    RnumBodies = len(motionProxy.getBodyNames(RShoulderPitch))
    LnumBodies = len(motionProxy.getBodyNames(LShoulderPitch))
    HeadPitchnum = len(motionProxy.getBodyNames(HeadPitch))
    HeadYawnum = len(motionProxy.getBodyNames(HeadPitch))
    LpTargetAngles = [0.0] * LnumBodies
    RpTargetAngles = [0.0] * RnumBodies
    HeadPitchTargetAngles = [-0.5] * HeadPitchnum 
    HeadYawTargetAngles = [-1.0] * HeadYawnum
    pMaxSpeedFraction = 0.5
    HeadPitchSpeed = 0.05
    HeadYawSpeed = 0.1
    motionProxy.post.angleInterpolationWithSpeed(RShoulderPitch, RpTargetAngles, pMaxSpeedFraction)
    motionProxy.post.angleInterpolationWithSpeed(LShoulderPitch, LpTargetAngles, pMaxSpeedFraction)
    motionProxy.post.angleInterpolationWithSpeed(HeadPitch, HeadPitchTargetAngles, HeadPitchSpeed)
    motionProxy.post.angleInterpolationWithSpeed(HeadYaw, HeadYawTargetAngles, HeadYawSpeed)
    
    #pMaxSpeedFraction = 0.3
    
    # Go to rest position
    #motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
