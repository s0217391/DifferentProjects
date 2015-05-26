#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + otherHunter[1]
	if otherHunter[1] != 0:
		temp1 = temp0 / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp0 = max( temp0 , temp1 )
	temp0 = temp0 + otherHunter[1]
	temp2 = prey[0] + dist
	temp2 = min( temp0 , temp1 )
	temp2 = min( dist , temp1 )
	temp0 = -1 * prey[0]
	temp2 = temp2 * otherHunter[0]
	temp2 = prey[0] + prey[1]
	temp3 = dist + otherHunter[0]
	if temp0 != 0:
		temp2 = temp3 % temp0
	else:
		temp2 = temp0
	temp2 = max( otherHunter[1] , otherHunter[1] )
	if otherHunter[1] != 0:
		temp0 = temp0 % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if otherHunter[0] != 0:
		temp2 = prey[1] / otherHunter[0]
	else:
		temp2 = otherHunter[0]
	temp3 = min( prey[1] , temp2 )
	return [ otherHunter[0] , temp2 ]
