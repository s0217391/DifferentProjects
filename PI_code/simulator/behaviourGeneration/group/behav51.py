#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist * prey[1]
	temp1 = prey[0] + dist
	temp2 = -1 * prey[1]
	temp3 = temp2 * dist
	if temp2 != 0:
		temp4 = otherHunter[1] % temp2
	else:
		temp4 = temp2
	temp1 = temp4 * temp2
	if otherHunter[0] != 0:
		temp1 = temp0 % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if temp3 != 0:
		temp2 = temp1 / temp3
	else:
		temp2 = temp3
	temp5 = max( temp3 , prey[1] )
	temp3 = max( dist , prey[0] )
	if temp5 != 0:
		temp0 = temp4 / temp5
	else:
		temp0 = temp5
	temp5 = dist * prey[1]
	temp1 = otherHunter[0] + temp5
	temp6 = max( dist , temp0 )
	return [ dist , prey[0] ]
