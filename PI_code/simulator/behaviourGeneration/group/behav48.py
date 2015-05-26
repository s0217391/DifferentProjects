#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , prey[1] )
	temp1 = prey[1] + prey[0]
	temp2 = max( temp1 , otherHunter[1] )
	temp0 = max( temp2 , otherHunter[0] )
	if temp1 != 0:
		temp2 = temp1 / temp1
	else:
		temp2 = temp1
	temp3 = dist + otherHunter[0]
	if temp3 != 0:
		temp1 = prey[1] / temp3
	else:
		temp1 = temp3
	if temp1 != 0:
		temp3 = temp1 % temp1
	else:
		temp3 = temp1
	temp1 = max( dist , otherHunter[0] )
	temp3 = temp0 * temp2
	temp1 = max( temp3 , otherHunter[1] )
	return [ dist , prey[0] ]
