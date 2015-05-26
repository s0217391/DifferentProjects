#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] * otherHunter[1]
	temp1 = -1 * temp0
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	temp1 = temp0 * otherHunter[1]
	temp0 = max( otherHunter[0] , prey[0] )
	temp0 = otherHunter[0] - temp1
	temp2 = prey[1] - otherHunter[1]
	temp1 = temp2 + temp2
	return [ prey[1] , otherHunter[1] ]
