#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = prey[0] % dist
	else:
		temp0 = dist
	temp1 = otherHunter[0] - prey[0]
	temp2 = max( otherHunter[0] , otherHunter[0] )
	temp3 = min( prey[1] , temp0 )
	temp2 = -1 * prey[0]
	temp1 = temp0 - otherHunter[1]
	if dist != 0:
		temp3 = prey[1] / dist
	else:
		temp3 = dist
	if prey[0] != 0:
		temp3 = dist % prey[0]
	else:
		temp3 = prey[0]
	if dist != 0:
		temp1 = prey[1] % dist
	else:
		temp1 = dist
	return [ prey[0] , dist ]
