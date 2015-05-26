#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > otherHunter[1] :
		temp0 = otherHunter[0] * otherHunter[1]
	else:
		temp0 = -1 * dist
	temp1 = min( prey[1] , prey[0] )
	if prey[0] != 0:
		temp0 = dist / prey[0]
	else:
		temp0 = prey[0]
	return [ temp1 , temp1 ]
