#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[0]
	temp1 = otherHunter[0] + prey[0]
	temp2 = max( otherHunter[0] , temp0 )
	if prey[1] > prey[1] :
		if otherHunter[1] != 0:
			temp0 = temp0 / otherHunter[1]
		else:
			temp0 = otherHunter[1]
	else:
		temp0 = min( otherHunter[0] , temp2 )
	temp1 = -1 * otherHunter[0]
	temp3 = dist * temp1
	temp4 = -1 * dist
	temp3 = max( otherHunter[0] , prey[1] )
	if temp2 != 0:
		temp5 = temp2 / temp2
	else:
		temp5 = temp2
	temp0 = temp5 - temp4
	temp0 = temp5 + otherHunter[0]
	return [ temp5 , temp4 ]
