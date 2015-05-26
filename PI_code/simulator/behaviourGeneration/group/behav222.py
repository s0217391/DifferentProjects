#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] + dist
	temp1 = min( dist , temp0 )
	temp1 = temp1 * otherHunter[1]
	temp0 = min( prey[1] , dist )
	if temp1 != 0:
		temp2 = temp1 / temp1
	else:
		temp2 = temp1
	temp2 = -1 * prey[0]
	temp1 = temp2 * prey[1]
	if prey[1] != 0:
		temp3 = temp1 / prey[1]
	else:
		temp3 = prey[1]
	return [ prey[0] , prey[0] ]
