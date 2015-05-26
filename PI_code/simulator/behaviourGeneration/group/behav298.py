#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = dist - otherHunter[0]
	temp1 = temp1 * otherHunter[1]
	temp1 = -1 * otherHunter[0]
	temp1 = max( temp1 , otherHunter[0] )
	temp0 = min( temp0 , temp1 )
	temp1 = min( dist , temp0 )
	temp2 = prey[0] * dist
	temp1 = max( prey[0] , temp2 )
	if temp0 != 0:
		temp1 = temp1 / temp0
	else:
		temp1 = temp0
	temp0 = min( dist , temp0 )
	temp0 = -1 * otherHunter[0]
	temp1 = otherHunter[0] - prey[0]
	temp1 = prey[0] + dist
	temp1 = min( temp1 , temp1 )
	return [ otherHunter[1] , prey[1] ]
