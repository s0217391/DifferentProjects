#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = prey[1] / dist
	else:
		temp0 = dist
	temp1 = -1 * prey[1]
	temp0 = max( prey[1] , temp0 )
	temp2 = temp0 + prey[1]
	temp3 = -1 * temp0
	temp1 = temp0 * dist
	temp1 = min( temp2 , temp1 )
	temp4 = temp2 * otherHunter[0]
	if temp3 != 0:
		temp2 = temp2 % temp3
	else:
		temp2 = temp3
	temp5 = min( prey[1] , otherHunter[0] )
	temp2 = dist + prey[1]
	temp1 = -1 * temp0
	if temp1 != 0:
		temp6 = prey[0] % temp1
	else:
		temp6 = temp1
	temp5 = min( temp4 , dist )
	temp2 = temp1 * temp2
	return [ otherHunter[1] , temp6 ]
