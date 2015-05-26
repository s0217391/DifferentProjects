#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] * dist
	temp1 = -1 * otherHunter[1]
	temp0 = otherHunter[1] * prey[0]
	if dist != 0:
		temp2 = dist / dist
	else:
		temp2 = dist
	temp2 = otherHunter[0] + prey[1]
	temp3 = temp2 - otherHunter[0]
	temp3 = temp2 + otherHunter[0]
	temp0 = min( prey[1] , dist )
	if temp2 > otherHunter[1] :
		if prey[1] != 0:
			temp1 = temp2 % prey[1]
		else:
			temp1 = prey[1]
	else:
		temp1 = temp1 + prey[1]
	return [ prey[0] , temp2 ]
