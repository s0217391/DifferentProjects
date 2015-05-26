#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist > otherHunter[0] :
		if dist != 0:
			temp0 = prey[1] / dist
		else:
			temp0 = dist
	else:
		temp0 = prey[1] + otherHunter[1]
	temp1 = temp0 * otherHunter[0]
	temp0 = max( temp0 , prey[0] )
	temp1 = -1 * temp0
	temp1 = -1 * prey[0]
	temp1 = max( prey[0] , prey[1] )
	temp0 = -1 * prey[1]
	return [ temp0 , temp0 ]
