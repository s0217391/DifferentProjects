#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > otherHunter[1] :
		temp0 = prey[0] - dist
	else:
		temp0 = dist * otherHunter[0]
	temp1 = prey[0] * prey[1]
	temp2 = min( prey[1] , otherHunter[0] )
	temp1 = -1 * otherHunter[0]
	temp0 = -1 * temp0
	temp2 = -1 * otherHunter[0]
	if temp0 != 0:
		temp3 = dist / temp0
	else:
		temp3 = temp0
	temp2 = -1 * otherHunter[0]
	temp1 = otherHunter[0] - temp0
	temp4 = temp3 * otherHunter[1]
	temp3 = prey[0] * otherHunter[0]
	if prey[1] != 0:
		temp2 = dist / prey[1]
	else:
		temp2 = prey[1]
	temp3 = max( otherHunter[0] , temp0 )
	temp5 = prey[0] + temp0
	return [ otherHunter[1] , temp4 ]
