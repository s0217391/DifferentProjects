#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] - otherHunter[1]
	temp1 = max( prey[1] , temp0 )
	if dist != 0:
		temp2 = otherHunter[0] % dist
	else:
		temp2 = dist
	temp2 = -1 * prey[1]
	return [ temp2 , prey[1] ]
