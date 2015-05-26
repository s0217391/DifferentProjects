#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = prey[1] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = -1 * prey[0]
	temp2 = temp1 * dist
	temp1 = -1 * otherHunter[0]
	temp2 = temp1 * prey[0]
	if temp0 != 0:
		temp1 = dist % temp0
	else:
		temp1 = temp0
	temp1 = max( temp2 , otherHunter[0] )
	temp0 = -1 * temp0
	temp0 = max( temp2 , otherHunter[1] )
	temp3 = max( otherHunter[0] , temp1 )
	temp3 = temp1 + temp1
	temp2 = max( dist , otherHunter[0] )
	return [ otherHunter[1] , otherHunter[1] ]
