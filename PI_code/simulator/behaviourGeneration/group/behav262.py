#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[0]
	if dist > prey[1] :
		temp1 = max( prey[1] , prey[0] )
	else:
		temp1 = temp0 + dist
	temp2 = max( prey[0] , temp0 )
	temp1 = max( temp2 , otherHunter[1] )
	temp3 = -1 * dist
	if otherHunter[1] != 0:
		temp2 = temp0 % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp1 = -1 * temp2
	temp3 = temp2 * otherHunter[1]
	if temp1 != 0:
		temp3 = temp0 % temp1
	else:
		temp3 = temp1
	if temp2 != 0:
		temp2 = temp2 % temp2
	else:
		temp2 = temp2
	temp4 = prey[1] - temp1
	temp4 = temp1 + otherHunter[1]
	return [ otherHunter[1] , otherHunter[0] ]
