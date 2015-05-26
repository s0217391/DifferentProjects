#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] - otherHunter[1]
	temp1 = max( otherHunter[1] , prey[0] )
	temp0 = otherHunter[0] + prey[1]
	temp2 = max( prey[1] , otherHunter[0] )
	if prey[0] != 0:
		temp3 = dist / prey[0]
	else:
		temp3 = prey[0]
	temp2 = -1 * prey[0]
	temp0 = max( dist , prey[0] )
	return [ temp0 , otherHunter[1] ]
