# -*- encoding: UTF-8 -*-

import almath
import motion
import argparse
import time
import sys
#import sensorsTouch
import pickle
import os
import copy
#import matplotlib.pyplot as plt

from naoqi import ALProxy
from naoqi import ALProxy
from naoqi import ALBroker

def interpolate(motionProxy, movementsList):
	effectorList = ["RHand","Torso","RArm"]
	frame = motion.FRAME_ROBOT
	axisMask = almath.AXIS_MASK_X + almath.AXIS_MASK_Y + almath.AXIS_MASK_Z
	times=[]

	for i in range(len(movementsList)):
		times.append(i+0.5)
	#print times

	motionProxy.positionInterpolation(effectorList[2], frame, movementsList,axisMask, times, False)

def heart(motionProxy, tts):
	movementsList = [[0.0, -0.025, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.005, 0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.00, 0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.005, 0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.005, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.005, -0.007, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.0, 0.002, 0.004, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.003, -0.007, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.002, 0.010, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.004, -0.002, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.001, 0.007, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.005, 0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.005, 0.00, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.005, -0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.0, -0.020, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

def klobuk(motionProxy, tts):
	movementsList = [[0.0, 0.0, 0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.005, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.0, 0.02, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.01, -0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.01, 0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.0, -0.02, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.005, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.0, -0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.03, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

def okuliare(motionProxy, tts):
	movementsList = [[0.0, 0.0, 0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.009, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.0, -0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.009, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.0, 0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.0, -0.01, 0.015, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.01, -0.015, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.02, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.0, -0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.009, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.0, 0.0, 0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.009, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.01, 0.015, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

def hory(motionProxy, tts):
	movementsList = [[0.0, -0.01, 0.025, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.005, -0.015, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.01, 0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.005, -0.015, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.03, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)


def hviezda(motionProxy, tts):
	movementsList = [[0.0, -0.01, 0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.01, -0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.005, 0.01, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.005, 0.01, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.01, -0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.01, 0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.005, -0.01, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.005, -0.01, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

def house(motionProxy, tts):
	movementsList = [[0.0, -0.02, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.02, 0.02, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.02, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.01, 0.01, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.01, -0.01, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.0, -0.02, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, -0.02, 0.02, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.0, 0.0, -0.02, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

