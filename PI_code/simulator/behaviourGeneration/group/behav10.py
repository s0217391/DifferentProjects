#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( dist , otherHunter[0] )
	temp1 = -1 * otherHunter[1]
	temp1 = temp0 + dist
	temp0 = dist * otherHunter[1]
	temp2 = min( prey[0] , dist )
	temp2 = min( otherHunter[0] , otherHunter[0] )
	temp3 = otherHunter[1] - temp2
	temp2 = temp0 + temp3
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	temp2 = otherHunter[1] + dist
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp4 = otherHunter[0] + temp0
	temp5 = -1 * temp2
	return [ otherHunter[0] , prey[0] ]
