#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[1] , prey[1] )
	temp1 = temp0 + otherHunter[1]
	temp2 = prey[1] - temp1
	if otherHunter[0] != 0:
		temp0 = temp2 / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp0 = -1 * temp1
	temp0 = min( temp0 , temp1 )
	temp3 = temp2 - temp1
	if dist != 0:
		temp2 = temp2 % dist
	else:
		temp2 = dist
	if prey[1] != 0:
		temp1 = temp0 % prey[1]
	else:
		temp1 = prey[1]
	temp0 = max( temp2 , dist )
	temp4 = dist + temp0
	temp3 = prey[1] * otherHunter[0]
	return [ temp0 , temp0 ]
