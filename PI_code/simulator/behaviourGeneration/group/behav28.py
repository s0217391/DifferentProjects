#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = dist % prey[0]
	else:
		temp0 = prey[0]
	temp1 = temp0 * dist
	temp1 = temp0 + dist
	if temp1 != 0:
		temp2 = temp1 % temp1
	else:
		temp2 = temp1
	temp2 = temp0 * otherHunter[0]
	temp2 = temp2 + otherHunter[0]
	temp3 = max( temp0 , temp2 )
	temp0 = -1 * temp2
	if otherHunter[0] != 0:
		temp1 = temp2 / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp1 = min( prey[1] , dist )
	temp2 = otherHunter[1] - dist
	temp0 = min( otherHunter[0] , temp1 )
	temp1 = max( temp0 , prey[1] )
	temp3 = max( temp1 , prey[0] )
	temp3 = otherHunter[1] * prey[0]
	temp2 = temp0 + temp2
	temp1 = temp2 - otherHunter[0]
	return [ temp3 , temp2 ]
