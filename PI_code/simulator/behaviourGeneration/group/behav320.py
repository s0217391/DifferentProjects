#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[0]
	if otherHunter[1] != 0:
		temp1 = dist / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if temp1 != 0:
		temp0 = dist % temp1
	else:
		temp0 = temp1
	if temp1 != 0:
		temp0 = dist % temp1
	else:
		temp0 = temp1
	temp0 = max( otherHunter[1] , otherHunter[0] )
	temp2 = prey[1] + temp1
	temp1 = otherHunter[0] - temp0
	return [ temp2 , temp0 ]
