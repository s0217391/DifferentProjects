#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = otherHunter[1] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = temp0 - otherHunter[0]
	temp2 = max( prey[1] , temp1 )
	temp0 = max( dist , prey[0] )
	temp2 = temp2 * temp2
	temp3 = prey[0] + temp0
	if dist != 0:
		temp4 = dist / dist
	else:
		temp4 = dist
	if otherHunter[0] != 0:
		temp0 = temp0 / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp5 = prey[0] - temp1
	if temp1 != 0:
		temp5 = temp0 / temp1
	else:
		temp5 = temp1
	temp3 = max( prey[0] , temp2 )
	temp4 = -1 * dist
	temp2 = max( temp4 , temp1 )
	if prey[0] != 0:
		temp5 = temp1 % prey[0]
	else:
		temp5 = prey[0]
	return [ otherHunter[0] , dist ]
