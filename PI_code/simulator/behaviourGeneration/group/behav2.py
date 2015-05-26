#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > otherHunter[0] :
		if prey[0] != 0:
			temp0 = dist / prey[0]
		else:
			temp0 = prey[0]
	else:
		temp0 = min( prey[0] , otherHunter[1] )
	temp1 = prey[0] * temp0
	temp1 = -1 * prey[1]
	temp1 = prey[1] + otherHunter[1]
	temp0 = temp0 - otherHunter[0]
	if temp1 != 0:
		temp1 = prey[0] / temp1
	else:
		temp1 = temp1
	return [ temp0 , temp1 ]
