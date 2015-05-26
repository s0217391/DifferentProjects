#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + dist
	temp1 = max( prey[1] , dist )
	if temp1 != 0:
		temp2 = temp1 % temp1
	else:
		temp2 = temp1
	temp0 = dist - prey[1]
	temp3 = max( prey[1] , temp2 )
	temp3 = min( temp1 , temp0 )
	if otherHunter[0] != 0:
		temp0 = temp1 / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp0 = temp2 - prey[1]
	temp3 = otherHunter[0] * otherHunter[0]
	temp4 = temp2 * otherHunter[0]
	temp1 = min( otherHunter[0] , temp3 )
	if temp1 != 0:
		temp4 = temp2 / temp1
	else:
		temp4 = temp1
	temp3 = otherHunter[1] - prey[1]
	temp0 = min( otherHunter[0] , otherHunter[0] )
	if temp1 != 0:
		temp0 = prey[1] / temp1
	else:
		temp0 = temp1
	if prey[0] > otherHunter[0] :
		temp5 = -1 * temp0
	else:
		temp5 = -1 * temp4
	temp5 = max( temp2 , temp5 )
	temp5 = max( temp1 , temp5 )
	temp4 = dist * prey[0]
	temp1 = min( prey[1] , otherHunter[1] )
	temp2 = temp2 + otherHunter[1]
	return [ temp5 , prey[1] ]
