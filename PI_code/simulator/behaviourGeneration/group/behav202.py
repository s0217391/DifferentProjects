#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * prey[1]
	temp1 = max( otherHunter[0] , otherHunter[1] )
	if otherHunter[1] != 0:
		temp0 = dist / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp0 = temp0 * prey[1]
	return [ prey[0] , prey[0] ]
