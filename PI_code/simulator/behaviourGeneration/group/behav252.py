#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[0] , otherHunter[0] )
	temp1 = otherHunter[1] * otherHunter[0]
	temp2 = -1 * temp1
	temp1 = temp1 - otherHunter[1]
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	temp3 = temp1 - prey[0]
	if prey[1] != 0:
		temp2 = otherHunter[0] / prey[1]
	else:
		temp2 = prey[1]
	temp3 = min( prey[0] , temp2 )
	temp2 = otherHunter[1] + temp1
	temp4 = temp3 + temp2
	temp5 = temp1 * temp0
	temp3 = temp3 * temp5
	temp1 = dist - temp1
	return [ prey[1] , temp0 ]
