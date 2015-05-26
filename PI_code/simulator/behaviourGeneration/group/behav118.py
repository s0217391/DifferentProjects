#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] - prey[0]
	temp1 = max( otherHunter[0] , prey[0] )
	temp2 = min( otherHunter[0] , prey[0] )
	if temp0 != 0:
		temp2 = otherHunter[1] / temp0
	else:
		temp2 = temp0
	temp2 = -1 * prey[1]
	temp0 = -1 * prey[0]
	temp0 = dist * otherHunter[0]
	if prey[0] != 0:
		temp3 = temp2 % prey[0]
	else:
		temp3 = prey[0]
	return [ otherHunter[0] , temp2 ]
