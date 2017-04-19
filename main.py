# -*- encoding: UTF-8 -*-

import almath
import motion
import argparse
import time
import sys
# import sensorsTouch
import pickle
import os
import copy
# import matplotlib.pyplot as plt

from naoqi import ALProxy
from naoqi import ALProxy
from naoqi import ALBroker

import Alphabet
import Pictures


# Move hand UP
def moveReady(motionProxy, offset):
    motionProxy.setStiffnesses("RArm", 1.0)
    fractionMaxSpeed = 0.2

    # position Wrist
    angle = 0.6  # 1.57
    motionProxy.setAngles("RWristYaw", angle, fractionMaxSpeed)

    # position Shoulder and Elbow
    angleShoulderPitch = -0.1779019832611084
    motionProxy.setAngles("RShoulderPitch", angleShoulderPitch, fractionMaxSpeed)

    angleShoulderRoll = 0.0 - offset  # -0.7025980758666992
    motionProxy.setAngles("RShoulderRoll", angleShoulderRoll, fractionMaxSpeed)

    angleElbowRoll = 1.544616388
    motionProxy.setAngles("RElbowRoll", angleElbowRoll, fractionMaxSpeed)

    angleElbowPitch = 1.61137611389160156
    motionProxy.setAngles("RElbowYaw", angleElbowPitch, fractionMaxSpeed)


# Ready the hand Position
def inMove(motionProxy, offset):
    motionProxy.setStiffnesses("RArm", 1.0)
    fractionMaxSpeed = 0.2

    # position Wrist
    angle = 0.6  # 1.57
    motionProxy.setAngles("RWristYaw", angle, fractionMaxSpeed)

    # position Shoulder and Elbow
    angleShoulderPitch = -0.1779019832611084
    motionProxy.setAngles("RShoulderPitch", angleShoulderPitch, fractionMaxSpeed)

    angleShoulderRoll = 0.0 - offset  # -0.7025980758666992
    motionProxy.setAngles("RShoulderRoll", angleShoulderRoll, fractionMaxSpeed)

    angleElbowRoll = 1.544616388
    motionProxy.setAngles("RElbowRoll", angleElbowRoll, fractionMaxSpeed)

    angleElbowPitch = 1.61137611389160156
    motionProxy.setAngles("RElbowYaw", angleElbowPitch, fractionMaxSpeed)


# Press hand towards whiteboard
def drawReady(motionProxy, offset):
    motionProxy.setStiffnesses("RArm", 1.0)
    fractionMaxSpeed = 0.2

    # position Wrist
    angle = 0.6  # 1.57
    motionProxy.setAngles("RWristYaw", angle, fractionMaxSpeed)

    # position Shoulder and Elbow
    angleShoulderPitch = -0.1779019832611084
    motionProxy.setAngles("RShoulderPitch", angleShoulderPitch, fractionMaxSpeed)

    angleShoulderRoll = 0.0 - offset  # -0.7025980758666992
    motionProxy.setAngles("RShoulderRoll", angleShoulderRoll, fractionMaxSpeed)

    angleElbowRoll = 1.4618859100341797
    motionProxy.setAngles("RElbowRoll", angleElbowRoll, fractionMaxSpeed)

    angleElbowPitch = 1.61137611389160156
    motionProxy.setAngles("RElbowYaw", angleElbowPitch, fractionMaxSpeed)


# use transform to write letter
def reproduceMovement(motionProxy, letter, tty):
    if (letter == "A"):
        Alphabet.A(motionProxy, tty)
    elif (letter == "B"):
        Alphabet.B(motionProxy, tty)
    elif (letter == "C"):
        Alphabet.C(motionProxy, tty)
    elif (letter == "D"):
        Alphabet.D(motionProxy, tty)
    elif (letter == "E"):
        Alphabet.E(motionProxy, tty)
    elif (letter == "F"):
        Alphabet.F(motionProxy, tty)
    elif (letter == "G"):
        Alphabet.G(motionProxy, tty)
    elif (letter == "H"):
        Alphabet.H(motionProxy, tty)
    elif (letter == "I"):
        Alphabet.I(motionProxy, tty)
    elif (letter == "J"):
        Alphabet.J(motionProxy, tty)
    elif (letter == "K"):
        Alphabet.K(motionProxy, tty)
    elif (letter == "L"):
        Alphabet.L(motionProxy, tty)
    elif (letter == "M"):
        Alphabet.M(motionProxy, tty)
    elif (letter == "N"):
        Alphabet.N(motionProxy, tty)
    elif (letter == "O"):
        Alphabet.O(motionProxy, tty)
    elif (letter == "P"):
        Alphabet.P(motionProxy, tty)
    elif (letter == "Q"):
        Alphabet.Q(motionProxy, tty)
    elif (letter == "R"):
        Alphabet.R(motionProxy, tty)
    elif (letter == "S"):
        Alphabet.S(motionProxy, tty)
    elif (letter == "T"):
        Alphabet.T(motionProxy, tty)
    elif (letter == "U"):
        Alphabet.U(motionProxy, tty)
    elif (letter == "V"):
        Alphabet.V(motionProxy, tty)
    elif (letter == "W"):
        Alphabet.W(motionProxy, tty)
    elif (letter == "X"):
        Alphabet.X(motionProxy, tty)
    elif (letter == "Y"):
        Alphabet.Y(motionProxy, tty)
    elif (letter == "Z"):
        Alphabet.Z(motionProxy, tty)


# Write each letter individualy
def writeWord(motionProxy, word, tts):
    word = word.upper()
    off = 0
    for i in word:
        if (i != " "):
            drawReady(motionProxy, off * 0.12) # Ready the hand
            time.sleep(1)
            reproduceMovement(motionProxy, i, tts) # Write letter
            time.sleep(1)

            fractionMaxSpeed = 0.2
            angleElbowRoll = 1.544616388 # pull hand away from whiteboard
            motionProxy.setAngles("RElbowRoll", angleElbowRoll, fractionMaxSpeed)
            time.sleep(1)

            off = off + 1
            moveReady(motionProxy, off * 0.12) # Move hand little bit right (away from whiteboard)
            time.sleep(1)
            inMove(motionProxy, off * 0.12)
            time.sleep(1)


def main(robotIP, PORT=9559):
    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    # myBroker = ALBroker("myBroker",
    #   "0.0.0.0",   # listen to anyone
    #   0,           # find a free port and use it
    #  robotIP,          # parent broker IP
    #  PORT)        # parent broker port

    # StartProxies
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    tty = ALProxy("ALTextToSpeech", robotIP, PORT)

    # Send robot to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    # Loop for the broker
    try:
        drawReady(motionProxy, 0.0)
        time.sleep(2)

        writeWord(motionProxy, "FUN", tty)

    except KeyboardInterrupt:
        # Go to rest position
        motionProxy.rest()
        print "Interrupted by user, shutting down"
        # myBroker.shutdown()
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.109", help="Robot ip address")
    # parser.add_argument("--ip", type=str, default="10.10.19.51",help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
