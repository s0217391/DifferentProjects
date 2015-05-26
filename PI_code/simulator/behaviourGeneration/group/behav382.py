#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * dist
	temp1 = temp0 * otherHunter[1]
	temp0 = otherHunter[1] * temp0
	temp2 = temp0 + dist
	temp3 = min( otherHunter[1] , otherHunter[1] )
	if prey[1] != 0:
		temp4 = prey[0] % prey[1]
	else:
		temp4 = prey[1]
	temp1 = max( dist , temp2 )
	temp2 = temp4 + dist
	temp4 = min( temp1 , prey[1] )
	temp4 = -1 * otherHunter[1]
	temp5 = temp2 + prey[1]
	temp0 = otherHunter[1] + otherHunter[1]
	temp3 = max( temp2 , temp3 )
	temp0 = max( temp0 , dist )
	return [ temp4 , temp5 ]
