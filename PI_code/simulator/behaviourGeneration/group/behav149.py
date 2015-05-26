#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = dist / prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[1] * otherHunter[0]
	if otherHunter[0] != 0:
		temp2 = prey[0] / otherHunter[0]
	else:
		temp2 = otherHunter[0]
	if temp1 != 0:
		temp1 = dist % temp1
	else:
		temp1 = temp1
	temp2 = max( temp2 , otherHunter[1] )
	temp3 = max( dist , dist )
	if otherHunter[0] != 0:
		temp1 = temp1 % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if dist != 0:
		temp4 = temp3 % dist
	else:
		temp4 = dist
	temp1 = max( temp4 , otherHunter[0] )
	temp0 = -1 * temp0
	if otherHunter[1] != 0:
		temp5 = dist % otherHunter[1]
	else:
		temp5 = otherHunter[1]
	temp5 = max( temp5 , temp3 )
	return [ temp0 , temp0 ]
