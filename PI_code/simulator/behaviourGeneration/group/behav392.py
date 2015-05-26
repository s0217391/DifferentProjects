#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[1]
	temp1 = temp0 - prey[0]
	temp2 = temp1 * otherHunter[0]
	temp1 = min( temp0 , temp1 )
	if temp1 != 0:
		temp1 = dist / temp1
	else:
		temp1 = temp1
	if temp0 != 0:
		temp3 = temp1 % temp0
	else:
		temp3 = temp0
	temp4 = max( prey[1] , dist )
	temp1 = max( otherHunter[0] , otherHunter[1] )
	temp1 = otherHunter[1] - temp1
	temp1 = -1 * otherHunter[0]
	temp3 = temp0 + temp0
	temp5 = -1 * temp0
	temp2 = min( prey[1] , temp3 )
	temp1 = max( temp5 , temp0 )
	return [ temp3 , temp2 ]
