#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[1] , prey[1] )
	if prey[1] > otherHunter[1] :
		temp1 = otherHunter[0] + prey[0]
	else:
		temp1 = max( otherHunter[1] , dist )
	temp2 = max( temp0 , otherHunter[1] )
	temp1 = dist - temp1
	temp3 = -1 * temp1
	temp0 = max( temp2 , temp0 )
	temp1 = otherHunter[1] - otherHunter[0]
	temp4 = min( otherHunter[1] , otherHunter[1] )
	if temp1 != 0:
		temp0 = prey[0] % temp1
	else:
		temp0 = temp1
	temp3 = prey[0] + dist
	if temp3 != 0:
		temp2 = temp3 % temp3
	else:
		temp2 = temp3
	temp2 = max( prey[0] , temp0 )
	temp3 = otherHunter[0] - otherHunter[0]
	temp5 = -1 * temp0
	temp6 = -1 * otherHunter[0]
	return [ temp3 , otherHunter[1] ]
