#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[1] , prey[1] )
	temp1 = prey[1] + temp0
	temp0 = max( temp1 , otherHunter[1] )
	temp2 = -1 * prey[0]
	temp3 = -1 * otherHunter[1]
	if temp2 != 0:
		temp2 = temp3 % temp2
	else:
		temp2 = temp2
	temp1 = temp2 * prey[1]
	temp2 = max( temp0 , temp1 )
	temp0 = prey[0] + temp0
	if dist != 0:
		temp1 = dist % dist
	else:
		temp1 = dist
	return [ otherHunter[1] , temp2 ]
