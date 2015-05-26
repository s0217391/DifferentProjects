#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = dist / prey[1]
	else:
		temp0 = prey[1]
	temp1 = temp0 - dist
	temp1 = max( otherHunter[1] , prey[1] )
	temp1 = temp0 - temp0
	temp2 = -1 * temp1
	if temp1 != 0:
		temp1 = prey[0] / temp1
	else:
		temp1 = temp1
	temp2 = temp2 + prey[1]
	temp1 = min( temp0 , temp1 )
	temp3 = min( temp0 , dist )
	if prey[0] != 0:
		temp2 = otherHunter[0] % prey[0]
	else:
		temp2 = prey[0]
	return [ prey[1] , prey[1] ]
