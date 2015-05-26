#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[0] , prey[1] )
	temp1 = max( prey[0] , prey[1] )
	temp0 = temp0 * dist
	temp1 = min( otherHunter[1] , otherHunter[0] )
	temp0 = -1 * dist
	if dist != 0:
		temp1 = otherHunter[1] / dist
	else:
		temp1 = dist
	temp0 = otherHunter[1] - temp1
	if dist != 0:
		temp0 = temp0 % dist
	else:
		temp0 = dist
	temp1 = max( otherHunter[0] , temp0 )
	temp0 = max( prey[0] , prey[0] )
	temp2 = min( otherHunter[0] , otherHunter[1] )
	temp0 = temp1 - dist
	return [ temp2 , temp2 ]
