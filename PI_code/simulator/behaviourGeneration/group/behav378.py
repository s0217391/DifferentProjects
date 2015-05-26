#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] + prey[0]
	temp1 = max( temp0 , otherHunter[1] )
	temp0 = dist * temp1
	temp1 = temp0 * otherHunter[1]
	temp1 = max( prey[1] , prey[0] )
	temp1 = -1 * otherHunter[0]
	if prey[1] > prey[0] :
		if temp0 != 0:
			temp2 = temp1 % temp0
		else:
			temp2 = temp0
	else:
		if dist > prey[0] :
			temp2 = otherHunter[0] * otherHunter[1]
		else:
			temp2 = prey[1] * temp1
	if otherHunter[0] > prey[0] :
		temp0 = prey[1] * dist
	else:
		if dist != 0:
			temp0 = dist / dist
		else:
			temp0 = dist
	return [ dist , temp0 ]
