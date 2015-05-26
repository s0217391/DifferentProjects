#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] - dist
	temp1 = -1 * dist
	temp2 = prey[0] - temp1
	temp2 = max( prey[0] , prey[1] )
	temp1 = min( temp2 , prey[0] )
	temp0 = -1 * temp0
	temp1 = temp0 * otherHunter[0]
	temp1 = max( temp1 , prey[1] )
	temp1 = prey[0] - otherHunter[0]
	temp1 = temp2 * prey[1]
	temp3 = prey[1] + temp1
	temp4 = -1 * otherHunter[0]
	if prey[0] != 0:
		temp3 = otherHunter[0] % prey[0]
	else:
		temp3 = prey[0]
	temp2 = temp0 - otherHunter[0]
	temp1 = -1 * temp2
	return [ temp1 , temp4 ]
