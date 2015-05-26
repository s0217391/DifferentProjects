#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist + dist
	temp1 = otherHunter[0] - dist
	temp2 = temp0 * otherHunter[0]
	if temp1 != 0:
		temp1 = temp1 % temp1
	else:
		temp1 = temp1
	if temp2 != 0:
		temp1 = temp1 / temp2
	else:
		temp1 = temp2
	temp1 = -1 * temp2
	temp3 = -1 * prey[0]
	temp2 = max( otherHunter[0] , temp0 )
	if temp2 != 0:
		temp1 = prey[1] % temp2
	else:
		temp1 = temp2
	temp0 = temp0 + temp2
	if otherHunter[0] != 0:
		temp4 = temp0 / otherHunter[0]
	else:
		temp4 = otherHunter[0]
	return [ otherHunter[0] , temp1 ]
