#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + otherHunter[1]
	temp1 = otherHunter[0] + dist
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	temp1 = min( prey[0] , dist )
	if prey[0] > otherHunter[1] :
		temp1 = max( otherHunter[1] , temp1 )
	else:
		temp1 = max( dist , temp1 )
	temp2 = -1 * prey[1]
	if prey[0] != 0:
		temp3 = otherHunter[1] / prey[0]
	else:
		temp3 = prey[0]
	temp4 = -1 * otherHunter[1]
	temp1 = min( temp0 , dist )
	temp0 = max( otherHunter[0] , temp1 )
	if temp1 != 0:
		temp3 = temp3 % temp1
	else:
		temp3 = temp1
	return [ temp0 , prey[1] ]
