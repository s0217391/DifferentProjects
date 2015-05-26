#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = min( prey[1] , prey[0] )
	temp2 = max( prey[1] , temp0 )
	temp2 = -1 * otherHunter[1]
	return [ temp1 , temp2 ]
