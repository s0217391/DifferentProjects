#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = otherHunter[1] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * prey[1]
	temp2 = min( prey[0] , temp0 )
	temp0 = min( prey[1] , prey[1] )
	if temp0 != 0:
		temp2 = temp2 / temp0
	else:
		temp2 = temp0
	temp0 = prey[1] * temp1
	temp1 = min( prey[1] , dist )
	temp0 = otherHunter[0] - temp1
	temp0 = -1 * prey[0]
	temp2 = max( otherHunter[0] , temp2 )
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	if temp0 != 0:
		temp1 = otherHunter[1] % temp0
	else:
		temp1 = temp0
	temp1 = min( prey[0] , otherHunter[1] )
	temp0 = -1 * otherHunter[1]
	temp0 = temp1 - temp2
	if temp1 != 0:
		temp3 = dist / temp1
	else:
		temp3 = temp1
	temp0 = min( temp3 , temp1 )
	if prey[1] != 0:
		temp1 = temp0 % prey[1]
	else:
		temp1 = prey[1]
	temp0 = max( temp0 , prey[1] )
	return [ temp0 , prey[0] ]
