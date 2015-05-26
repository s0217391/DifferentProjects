#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[0] , prey[1] )
	if otherHunter[0] != 0:
		temp1 = prey[1] / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp2 = max( dist , dist )
	temp2 = dist - prey[0]
	temp2 = -1 * prey[0]
	temp1 = temp1 * temp2
	temp1 = otherHunter[0] - otherHunter[1]
	if otherHunter[0] != 0:
		temp1 = temp0 % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if temp1 != 0:
		temp0 = temp2 % temp1
	else:
		temp0 = temp1
	if temp0 > temp2 :
		if temp2 != 0:
			temp3 = prey[1] / temp2
		else:
			temp3 = temp2
	else:
		temp3 = dist - temp0
	if prey[1] > temp1 :
		if otherHunter[0] != 0:
			temp2 = temp1 / otherHunter[0]
		else:
			temp2 = otherHunter[0]
	else:
		if prey[0] != 0:
			temp2 = temp0 / prey[0]
		else:
			temp2 = prey[0]
	temp1 = otherHunter[0] * prey[0]
	temp0 = max( prey[0] , temp0 )
	if otherHunter[0] != 0:
		temp1 = temp0 / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp2 = otherHunter[0] - temp1
	temp1 = temp0 - temp2
	temp0 = prey[0] - otherHunter[1]
	return [ dist , temp0 ]
