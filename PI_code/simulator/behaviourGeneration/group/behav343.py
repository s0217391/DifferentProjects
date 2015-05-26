#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = dist / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = max( prey[0] , otherHunter[1] )
	temp2 = temp1 + dist
	temp0 = dist + otherHunter[0]
	temp3 = dist + dist
	return [ otherHunter[1] , otherHunter[0] ]
