#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] - otherHunter[1]
	temp1 = prey[1] + dist
	if prey[0] != 0:
		temp2 = temp1 / prey[0]
	else:
		temp2 = prey[0]
	temp3 = prey[0] + prey[0]
	temp3 = -1 * otherHunter[0]
	if temp3 != 0:
		temp0 = prey[0] % temp3
	else:
		temp0 = temp3
	temp1 = -1 * temp3
	if otherHunter[0] != 0:
		temp3 = prey[1] % otherHunter[0]
	else:
		temp3 = otherHunter[0]
	temp4 = temp0 - otherHunter[0]
	temp0 = min( otherHunter[1] , temp2 )
	return [ temp2 , otherHunter[0] ]
