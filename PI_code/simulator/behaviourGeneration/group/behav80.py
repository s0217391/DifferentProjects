#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , prey[0] )
	temp1 = min( temp0 , prey[1] )
	if temp0 > prey[1] :
		temp1 = -1 * temp1
	else:
		temp1 = prey[0] * otherHunter[1]
	temp0 = dist - prey[1]
	temp1 = temp1 - dist
	temp0 = temp1 - prey[1]
	return [ temp0 , temp0 ]
