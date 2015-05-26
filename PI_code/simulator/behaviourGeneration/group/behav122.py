#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = otherHunter[0] / dist
	else:
		temp0 = dist
	temp1 = -1 * temp0
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	temp0 = min( temp0 , prey[1] )
	temp1 = min( temp1 , otherHunter[1] )
	return [ otherHunter[0] , prey[1] ]
