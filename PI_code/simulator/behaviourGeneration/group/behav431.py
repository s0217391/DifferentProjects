#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist - prey[1]
	temp1 = -1 * prey[1]
	temp2 = -1 * temp1
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	temp0 = -1 * temp0
	temp1 = max( prey[0] , otherHunter[0] )
	temp1 = -1 * otherHunter[1]
	temp3 = temp0 + temp0
	temp1 = max( prey[0] , dist )
	return [ temp1 , temp2 ]
