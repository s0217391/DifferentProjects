#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = dist % prey[1]
	else:
		temp0 = prey[1]
	temp1 = min( prey[0] , dist )
	if otherHunter[1] != 0:
		temp1 = prey[1] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp0 = dist - dist
	if temp1 != 0:
		temp2 = otherHunter[1] % temp1
	else:
		temp2 = temp1
	temp0 = otherHunter[0] - prey[0]
	temp3 = -1 * prey[1]
	temp0 = -1 * otherHunter[1]
	temp4 = otherHunter[1] - prey[0]
	temp5 = max( temp3 , temp3 )
	return [ prey[0] , dist ]
