#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , otherHunter[1] )
	temp1 = min( dist , temp0 )
	temp0 = -1 * temp1
	if temp1 != 0:
		temp1 = temp1 / temp1
	else:
		temp1 = temp1
	temp0 = temp0 * dist
	temp0 = temp1 * prey[1]
	temp1 = max( temp0 , prey[1] )
	temp2 = max( otherHunter[1] , prey[0] )
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	temp0 = -1 * temp0
	temp0 = max( prey[1] , temp1 )
	if dist != 0:
		temp0 = dist / dist
	else:
		temp0 = dist
	return [ prey[1] , temp0 ]
