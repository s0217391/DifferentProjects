#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[1] , otherHunter[1] )
	temp1 = max( temp0 , otherHunter[0] )
	temp2 = temp1 * prey[1]
	if prey[0] != 0:
		temp1 = dist / prey[0]
	else:
		temp1 = prey[0]
	if temp2 != 0:
		temp1 = temp2 % temp2
	else:
		temp1 = temp2
	temp0 = max( dist , prey[0] )
	temp1 = dist + prey[0]
	temp0 = -1 * dist
	temp0 = temp2 * temp0
	temp3 = max( prey[1] , temp2 )
	temp2 = otherHunter[0] + temp1
	if otherHunter[1] != 0:
		temp2 = dist % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp2 = -1 * otherHunter[1]
	return [ dist , temp2 ]
