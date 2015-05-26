#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] * prey[1]
	temp1 = dist - temp0
	if temp1 != 0:
		temp2 = dist % temp1
	else:
		temp2 = temp1
	if prey[0] != 0:
		temp2 = dist % prey[0]
	else:
		temp2 = prey[0]
	temp2 = max( prey[0] , dist )
	temp2 = temp0 * otherHunter[0]
	if otherHunter[0] > temp0 :
		if prey[1] > prey[1] :
			temp1 = max( otherHunter[1] , temp1 )
		else:
			temp1 = temp2 - otherHunter[1]
	else:
		temp1 = dist + dist
	return [ dist , temp1 ]
