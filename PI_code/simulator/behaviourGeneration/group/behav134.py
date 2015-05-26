#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , otherHunter[0] )
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp1 = prey[1] * prey[0]
	temp0 = dist - temp0
	temp2 = dist * prey[0]
	temp0 = -1 * temp2
	temp3 = otherHunter[0] + otherHunter[1]
	temp1 = max( temp0 , dist )
	temp0 = -1 * otherHunter[1]
	temp0 = dist * otherHunter[1]
	if temp3 > temp0 :
		if prey[0] > temp1 :
			if temp1 > temp2 :
				temp1 = temp1 - otherHunter[0]
			else:
				temp1 = max( prey[0] , prey[0] )
		else:
			temp1 = temp1 + temp2
	else:
		temp1 = temp2 - temp3
	if temp0 > temp0 :
		temp2 = max( temp3 , temp0 )
	else:
		if prey[0] != 0:
			temp2 = temp0 % prey[0]
		else:
			temp2 = prey[0]
	temp1 = min( temp0 , otherHunter[0] )
	if temp1 > temp0 :
		if temp0 != 0:
			temp0 = otherHunter[0] / temp0
		else:
			temp0 = temp0
	else:
		temp0 = max( temp3 , prey[0] )
	return [ dist , prey[1] ]
