#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[0]
	temp1 = -1 * prey[1]
	temp1 = max( dist , temp0 )
	temp0 = max( temp0 , prey[0] )
	temp2 = dist + prey[1]
	temp2 = prey[0] + otherHunter[1]
	if otherHunter[1] != 0:
		temp0 = temp1 % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if temp0 != 0:
		temp3 = prey[1] % temp0
	else:
		temp3 = temp0
	if otherHunter[0] != 0:
		temp2 = otherHunter[1] / otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp1 = -1 * dist
	temp0 = -1 * prey[0]
	temp4 = temp0 + temp0
	temp0 = max( otherHunter[1] , otherHunter[1] )
	temp3 = min( prey[0] , temp1 )
	if prey[0] != 0:
		temp5 = temp4 % prey[0]
	else:
		temp5 = prey[0]
	temp6 = min( temp3 , otherHunter[0] )
	temp2 = max( temp5 , prey[1] )
	temp2 = max( temp5 , temp4 )
	temp0 = temp5 + otherHunter[0]
	return [ dist , prey[0] ]
