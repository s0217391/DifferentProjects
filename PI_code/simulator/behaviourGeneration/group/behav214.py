#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] - otherHunter[0]
	temp1 = min( prey[1] , otherHunter[1] )
	if dist > otherHunter[0] :
		if otherHunter[0] != 0:
			temp1 = otherHunter[1] % otherHunter[0]
		else:
			temp1 = otherHunter[0]
	else:
		temp1 = min( otherHunter[0] , prey[0] )
	temp1 = -1 * dist
	temp2 = -1 * dist
	temp0 = temp1 - prey[1]
	return [ temp0 , temp2 ]
