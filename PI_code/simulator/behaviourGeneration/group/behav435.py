#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , otherHunter[0] )
	temp1 = min( otherHunter[1] , prey[0] )
	if otherHunter[1] != 0:
		temp0 = dist % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp2 = dist + prey[1]
	temp0 = otherHunter[0] * temp2
	temp1 = temp1 * otherHunter[1]
	temp1 = max( otherHunter[1] , otherHunter[0] )
	if temp0 != 0:
		temp2 = dist % temp0
	else:
		temp2 = temp0
	if dist != 0:
		temp1 = temp0 % dist
	else:
		temp1 = dist
	temp2 = -1 * temp0
	if prey[0] != 0:
		temp1 = prey[0] % prey[0]
	else:
		temp1 = prey[0]
	return [ temp0 , prey[0] ]
