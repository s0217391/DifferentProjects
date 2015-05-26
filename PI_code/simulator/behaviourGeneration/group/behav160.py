#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = prey[0] % dist
	else:
		temp0 = dist
	if prey[0] != 0:
		temp1 = prey[1] % prey[0]
	else:
		temp1 = prey[0]
	temp1 = dist * otherHunter[0]
	temp0 = max( prey[0] , otherHunter[0] )
	if prey[1] != 0:
		temp1 = temp0 % prey[1]
	else:
		temp1 = prey[1]
	temp1 = prey[0] + otherHunter[1]
	temp1 = prey[1] + dist
	temp1 = dist + prey[1]
	temp1 = min( prey[1] , otherHunter[0] )
	temp2 = temp1 - temp0
	temp1 = prey[0] - temp2
	temp3 = -1 * temp1
	return [ otherHunter[1] , prey[1] ]
