#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = prey[0] / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = otherHunter[0] * prey[0]
	temp2 = prey[1] * temp1
	temp0 = otherHunter[0] * dist
	temp2 = min( prey[1] , temp2 )
	if temp0 != 0:
		temp0 = prey[0] % temp0
	else:
		temp0 = temp0
	temp2 = max( temp1 , prey[1] )
	temp1 = -1 * dist
	temp3 = temp0 * otherHunter[0]
	temp4 = min( prey[0] , prey[1] )
	temp3 = otherHunter[0] + otherHunter[1]
	if dist != 0:
		temp3 = temp0 % dist
	else:
		temp3 = dist
	temp4 = -1 * prey[1]
	if temp1 != 0:
		temp0 = prey[0] / temp1
	else:
		temp0 = temp1
	temp4 = temp3 + temp2
	temp0 = temp2 + temp0
	temp5 = min( otherHunter[0] , temp3 )
	temp1 = max( otherHunter[0] , temp0 )
	return [ temp4 , temp3 ]
