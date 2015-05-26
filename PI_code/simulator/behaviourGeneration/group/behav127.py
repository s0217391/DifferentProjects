#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = otherHunter[0] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = dist - otherHunter[1]
	temp1 = min( otherHunter[0] , temp0 )
	temp1 = max( dist , prey[1] )
	temp1 = min( otherHunter[0] , otherHunter[0] )
	temp2 = prey[1] + dist
	temp2 = prey[0] + otherHunter[0]
	if otherHunter[1] != 0:
		temp1 = dist / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if temp0 != 0:
		temp3 = temp0 % temp0
	else:
		temp3 = temp0
	temp2 = temp0 - temp3
	temp3 = min( dist , temp2 )
	if temp1 != 0:
		temp0 = temp1 % temp1
	else:
		temp0 = temp1
	temp4 = min( temp2 , temp0 )
	if otherHunter[0] != 0:
		temp5 = dist / otherHunter[0]
	else:
		temp5 = otherHunter[0]
	temp6 = -1 * temp2
	temp5 = max( temp0 , temp5 )
	return [ otherHunter[0] , temp1 ]
