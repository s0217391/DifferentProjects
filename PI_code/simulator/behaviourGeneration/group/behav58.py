#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = prey[1] / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = -1 * temp0
	if dist != 0:
		temp0 = temp1 % dist
	else:
		temp0 = dist
	return [ temp0 , otherHunter[1] ]
