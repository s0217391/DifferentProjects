#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , prey[1] )
	if prey[0] != 0:
		temp1 = otherHunter[0] % prey[0]
	else:
		temp1 = prey[0]
	temp0 = min( otherHunter[1] , temp1 )
	if otherHunter[0] != 0:
		temp2 = otherHunter[1] % otherHunter[0]
	else:
		temp2 = otherHunter[0]
	if dist != 0:
		temp1 = temp2 / dist
	else:
		temp1 = dist
	temp2 = -1 * temp1
	return [ prey[0] , temp2 ]
