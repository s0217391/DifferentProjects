#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist - prey[0]
	if dist != 0:
		temp1 = otherHunter[1] % dist
	else:
		temp1 = dist
	temp1 = max( prey[1] , temp0 )
	temp0 = -1 * otherHunter[1]
	return [ otherHunter[1] , otherHunter[0] ]
