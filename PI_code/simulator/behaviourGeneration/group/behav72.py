#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = dist / dist
	else:
		temp0 = dist
	temp1 = prey[0] * prey[0]
	temp2 = min( temp0 , prey[1] )
	temp1 = temp2 + prey[1]
	temp1 = -1 * temp0
	temp0 = otherHunter[0] - temp0
	temp0 = min( prey[0] , otherHunter[0] )
	temp1 = max( temp1 , prey[0] )
	temp1 = prey[0] - otherHunter[1]
	if temp0 != 0:
		temp3 = prey[0] / temp0
	else:
		temp3 = temp0
	return [ dist , dist ]
