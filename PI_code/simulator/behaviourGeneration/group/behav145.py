#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , prey[0] )
	temp1 = min( otherHunter[0] , otherHunter[0] )
	temp1 = -1 * prey[1]
	temp2 = dist * prey[0]
	if otherHunter[1] != 0:
		temp2 = prey[1] / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp0 = min( otherHunter[0] , otherHunter[1] )
	temp0 = temp2 * prey[1]
	temp1 = otherHunter[1] * prey[1]
	temp1 = dist - prey[0]
	temp2 = max( temp0 , temp2 )
	temp3 = prey[0] + temp1
	temp3 = temp0 * prey[1]
	temp2 = otherHunter[1] + temp3
	return [ dist , prey[0] ]
