#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , dist )
	if otherHunter[1] != 0:
		temp1 = prey[1] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp2 = -1 * temp1
	temp2 = min( temp0 , temp0 )
	temp2 = dist - temp2
	temp0 = otherHunter[0] + temp2
	temp3 = dist * otherHunter[1]
	temp4 = dist - otherHunter[1]
	if temp3 != 0:
		temp4 = temp0 / temp3
	else:
		temp4 = temp3
	if temp2 != 0:
		temp2 = prey[1] / temp2
	else:
		temp2 = temp2
	temp4 = -1 * dist
	temp1 = dist * prey[1]
	if temp2 != 0:
		temp0 = otherHunter[1] / temp2
	else:
		temp0 = temp2
	temp2 = prey[0] + otherHunter[1]
	if temp3 != 0:
		temp2 = otherHunter[0] / temp3
	else:
		temp2 = temp3
	temp3 = -1 * temp1
	return [ dist , dist ]
