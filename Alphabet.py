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

	motionProxy.positionInterpolation(effectorList[2], frame, movementsList, axisMask, times, False)

def A(motionProxy, tts):
	# movementsList = [[0.0, 0.0, -0.08, 0.0, 0.0, 0.0]]
	# interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.0, 0.0, -0.02, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0, 0.01, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.0, 0.0125, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

def B(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.008, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.0, -0.0045, -0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0045, -0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.0, 0.008, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.0, -0.008, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.0, -0.0045, -0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0045, -0.005, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.0, 0.008, 0.0, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

def C(motionProxy, tts):
	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.0, 0.0, 0.02, 0.0, 0.0, 0.0]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def D(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def E(motionProxy, tts):
	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.01, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.01, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def F(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.01, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def G(motionProxy, tts):
	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def H(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.012, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.012, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def I(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def J(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.004, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.004, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def K(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, 0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def L(motionProxy, tts):
	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def M(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.00625, -0.008, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.00625, 0.008, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def N(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, -0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def O(motionProxy, tts):
	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def P(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def Q(motionProxy, tts):
	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.004, -0.004, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.004, 0.004, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def R(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def S(motionProxy, tts):
	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def T(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.01, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.02, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def U(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, -0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def V(motionProxy, tts):
	movementsList = [[0.00, 0.00625, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.00, -0.00625, -0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.00, -0.00625, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)


def W(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.00, 0.00, -0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.00, -0.00625, 0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.00, -0.00625, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.00, 0.00, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)


def X(motionProxy, tts):
	movementsList = [[0.00, -0.0125, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.00625, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.00625, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, 0.0125, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def Y(motionProxy, tts):
	movementsList = [[0.00, 0.00, 0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

	movementsList = [[0.00, -0.00625, 0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.00, 0.00625, -0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.00, 0.00625, 0.01, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)

def Z(motionProxy, tts):
	movementsList = [[0.00, -0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.00, -0.0125, 0.02, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)
	movementsList = [[0.00, 0.0125, 0.00, 0.00, 0.00, 0.00]]
	interpolate(motionProxy, movementsList)
