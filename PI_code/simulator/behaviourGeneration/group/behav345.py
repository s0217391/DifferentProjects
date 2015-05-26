#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] + dist
	if otherHunter[0] != 0:
		temp1 = prey[1] / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp1 = min( otherHunter[0] , temp0 )
	temp1 = temp0 - otherHunter[0]
	if otherHunter[1] != 0:
		temp2 = prey[0] % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp3 = temp1 + temp1
	temp4 = temp3 - temp3
	temp0 = temp0 - temp0
	temp4 = max( prey[1] , otherHunter[1] )
	temp2 = -1 * temp4
	temp1 = temp0 * prey[0]
	return [ otherHunter[1] , otherHunter[1] ]
