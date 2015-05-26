#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] - otherHunter[1]
	temp1 = min( otherHunter[1] , prey[0] )
	if otherHunter[0] != 0:
		temp2 = prey[0] / otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp0 = min( prey[0] , temp0 )
	temp2 = -1 * otherHunter[1]
	temp1 = otherHunter[1] * otherHunter[1]
	temp2 = min( temp2 , otherHunter[0] )
	temp0 = max( otherHunter[1] , temp2 )
	temp3 = -1 * otherHunter[1]
	temp3 = dist - prey[1]
	temp4 = -1 * otherHunter[0]
	return [ prey[0] , temp1 ]
