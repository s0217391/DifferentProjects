#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	temp1 = prey[0] - otherHunter[0]
	temp2 = otherHunter[0] + dist
	if temp0 != 0:
		temp2 = temp1 / temp0
	else:
		temp2 = temp0
	temp1 = prey[1] + otherHunter[0]
	if prey[1] != 0:
		temp3 = prey[1] / prey[1]
	else:
		temp3 = prey[1]
	temp0 = min( temp2 , dist )
	temp4 = min( prey[1] , prey[0] )
	temp2 = min( otherHunter[0] , otherHunter[1] )
	if dist != 0:
		temp1 = temp4 % dist
	else:
		temp1 = dist
	temp0 = max( otherHunter[0] , temp2 )
	if otherHunter[1] != 0:
		temp1 = temp1 / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp2 = prey[1] - temp1
	temp2 = prey[1] * temp1
	temp3 = prey[0] * temp2
	temp3 = temp2 + dist
	temp5 = prey[1] * prey[1]
	temp5 = dist - otherHunter[1]
	return [ temp3 , temp5 ]
