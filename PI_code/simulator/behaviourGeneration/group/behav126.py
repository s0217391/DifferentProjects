#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] * prey[1]
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	if temp0 > otherHunter[1] :
		temp1 = prey[1] - prey[1]
	else:
		if otherHunter[1] != 0:
			temp1 = dist / otherHunter[1]
		else:
			temp1 = otherHunter[1]
	temp2 = dist - prey[0]
	temp0 = max( otherHunter[1] , temp2 )
	if temp1 != 0:
		temp1 = dist / temp1
	else:
		temp1 = temp1
	if dist != 0:
		temp2 = dist / dist
	else:
		temp2 = dist
	if dist != 0:
		temp2 = otherHunter[0] % dist
	else:
		temp2 = dist
	temp1 = prey[1] + prey[1]
	temp1 = min( otherHunter[0] , dist )
	temp2 = -1 * prey[0]
	temp0 = dist - temp2
	if temp0 != 0:
		temp1 = dist % temp0
	else:
		temp1 = temp0
	temp3 = -1 * prey[1]
	temp2 = max( temp2 , otherHunter[0] )
	temp2 = -1 * dist
	temp0 = temp2 + otherHunter[0]
	temp2 = otherHunter[1] - dist
	temp2 = max( otherHunter[1] , temp2 )
	temp0 = temp3 - otherHunter[0]
	temp4 = temp0 + dist
	temp4 = max( prey[0] , prey[0] )
	temp1 = -1 * temp4
	return [ dist , dist ]
