#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , otherHunter[0] )
	if prey[0] > prey[0] :
		temp1 = -1 * otherHunter[0]
	else:
		temp1 = prey[1] * prey[1]
	if prey[1] != 0:
		temp1 = otherHunter[1] / prey[1]
	else:
		temp1 = prey[1]
	if dist > prey[0] :
		temp2 = min( otherHunter[1] , temp0 )
	else:
		temp2 = -1 * otherHunter[1]
	temp2 = -1 * dist
	if temp1 != 0:
		temp3 = otherHunter[0] / temp1
	else:
		temp3 = temp1
	return [ dist , temp2 ]
