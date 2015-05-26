#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * dist
	temp1 = min( temp0 , otherHunter[0] )
	temp2 = max( temp1 , dist )
	if prey[1] != 0:
		temp2 = prey[0] % prey[1]
	else:
		temp2 = prey[1]
	temp2 = temp0 * temp1
	if otherHunter[1] != 0:
		temp2 = prey[0] / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	if temp2 != 0:
		temp3 = temp0 % temp2
	else:
		temp3 = temp2
	temp3 = min( temp1 , prey[0] )
	temp0 = min( temp0 , temp0 )
	temp3 = otherHunter[1] - temp0
	temp2 = temp1 * temp0
	temp2 = prey[0] * temp0
	return [ temp0 , otherHunter[0] ]
