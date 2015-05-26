#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , otherHunter[1] )
	if temp0 != 0:
		temp1 = otherHunter[1] % temp0
	else:
		temp1 = temp0
	temp0 = otherHunter[0] * prey[0]
	temp1 = max( prey[1] , otherHunter[0] )
	temp0 = max( temp0 , otherHunter[0] )
	temp1 = -1 * prey[0]
	return [ temp1 , otherHunter[0] ]
