#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[0]
	if prey[1] != 0:
		temp1 = prey[1] % prey[1]
	else:
		temp1 = prey[1]
	temp2 = temp0 + prey[1]
	temp1 = max( temp0 , temp1 )
	temp3 = min( temp0 , otherHunter[0] )
	if otherHunter[0] != 0:
		temp3 = temp1 / otherHunter[0]
	else:
		temp3 = otherHunter[0]
	temp4 = dist * temp1
	return [ temp1 , temp4 ]
