#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = dist % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	if temp1 != 0:
		temp2 = otherHunter[0] / temp1
	else:
		temp2 = temp1
	temp2 = prey[0] + otherHunter[1]
	temp0 = max( prey[1] , temp2 )
	temp1 = otherHunter[1] * otherHunter[0]
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = otherHunter[0] + temp2
	temp2 = temp1 - prey[0]
	temp0 = min( dist , temp2 )
	temp3 = temp1 + otherHunter[0]
	temp1 = max( temp3 , temp0 )
	temp1 = otherHunter[0] + dist
	temp3 = min( otherHunter[0] , prey[1] )
	temp2 = dist * dist
	temp1 = min( dist , otherHunter[1] )
	temp2 = temp0 - prey[0]
	return [ prey[0] , otherHunter[0] ]
