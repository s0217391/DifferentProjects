#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * dist
	if dist > otherHunter[0] :
		if prey[1] != 0:
			temp1 = prey[0] / prey[1]
		else:
			temp1 = prey[1]
	else:
		temp1 = max( prey[1] , dist )
	temp2 = temp1 * otherHunter[1]
	if otherHunter[1] != 0:
		temp1 = dist % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	return [ prey[1] , temp0 ]
