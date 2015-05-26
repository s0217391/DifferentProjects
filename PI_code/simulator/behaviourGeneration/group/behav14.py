#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = prey[1] % dist
	else:
		temp0 = dist
	temp1 = otherHunter[1] - dist
	temp0 = prey[0] * temp0
	temp0 = temp0 - temp0
	temp2 = -1 * prey[1]
	temp3 = max( dist , otherHunter[0] )
	temp2 = temp3 * temp2
	temp3 = max( prey[1] , otherHunter[1] )
	return [ prey[1] , otherHunter[0] ]
