#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] * prey[0]
	temp1 = temp0 + temp0
	temp2 = otherHunter[1] + otherHunter[0]
	temp0 = dist - prey[1]
	temp1 = otherHunter[0] * prey[0]
	temp3 = max( otherHunter[0] , dist )
	temp0 = -1 * temp1
	temp2 = temp1 * dist
	temp1 = temp2 - temp1
	temp2 = temp0 * temp1
	temp3 = temp2 * dist
	temp4 = dist - temp1
	if prey[1] > otherHunter[1] :
		temp0 = min( temp0 , temp0 )
	else:
		if prey[0] != 0:
			temp0 = temp2 % prey[0]
		else:
			temp0 = prey[0]
	temp3 = max( prey[0] , dist )
	if temp0 != 0:
		temp3 = dist / temp0
	else:
		temp3 = temp0
	return [ temp3 , otherHunter[0] ]
