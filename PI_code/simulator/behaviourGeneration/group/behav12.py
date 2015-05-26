#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = otherHunter[0] / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = prey[0] - otherHunter[1]
	temp0 = temp1 + dist
	if prey[1] != 0:
		temp2 = otherHunter[1] / prey[1]
	else:
		temp2 = prey[1]
	temp0 = otherHunter[1] - prey[0]
	temp3 = max( otherHunter[1] , otherHunter[1] )
	temp1 = -1 * temp2
	temp3 = temp1 * otherHunter[0]
	if temp3 > prey[0] :
		temp2 = otherHunter[1] - dist
	else:
		temp2 = prey[0] + temp2
	temp1 = -1 * prey[1]
	temp1 = temp0 + temp2
	temp2 = prey[1] - prey[1]
	temp2 = otherHunter[0] - temp3
	return [ prey[1] , temp2 ]
