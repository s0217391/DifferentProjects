#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[1]
	temp1 = otherHunter[1] + temp0
	temp1 = max( prey[1] , prey[0] )
	temp0 = otherHunter[0] + otherHunter[0]
	temp0 = otherHunter[0] * prey[0]
	temp1 = min( otherHunter[1] , temp1 )
	temp1 = prey[1] - temp1
	if temp1 != 0:
		temp2 = otherHunter[0] / temp1
	else:
		temp2 = temp1
	return [ prey[1] , prey[0] ]
