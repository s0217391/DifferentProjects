#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] - otherHunter[0]
	if prey[1] != 0:
		temp1 = prey[1] % prey[1]
	else:
		temp1 = prey[1]
	if otherHunter[1] != 0:
		temp1 = temp0 / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp0 = min( otherHunter[0] , dist )
	temp2 = temp0 - temp0
	if dist != 0:
		temp0 = otherHunter[0] % dist
	else:
		temp0 = dist
	temp0 = max( temp2 , otherHunter[0] )
	if prey[0] != 0:
		temp3 = temp0 / prey[0]
	else:
		temp3 = prey[0]
	if otherHunter[1] != 0:
		temp1 = temp0 % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if temp2 != 0:
		temp1 = otherHunter[1] / temp2
	else:
		temp1 = temp2
	temp1 = dist * prey[1]
	temp0 = max( temp0 , temp0 )
	temp4 = prey[1] * otherHunter[0]
	return [ prey[1] , temp2 ]
