#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( dist , dist )
	temp1 = -1 * prey[0]
	temp2 = otherHunter[0] * prey[1]
	if temp1 != 0:
		temp2 = dist % temp1
	else:
		temp2 = temp1
	if temp1 > temp2 :
		temp2 = -1 * temp1
	else:
		temp2 = max( temp1 , temp0 )
	temp3 = prey[1] - otherHunter[0]
	temp0 = max( temp1 , temp2 )
	if otherHunter[0] != 0:
		temp2 = prey[0] / otherHunter[0]
	else:
		temp2 = otherHunter[0]
	if otherHunter[0] != 0:
		temp1 = otherHunter[1] / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp3 = prey[0] - temp2
	if temp1 != 0:
		temp3 = otherHunter[1] % temp1
	else:
		temp3 = temp1
	temp3 = temp1 * temp1
	return [ prey[1] , otherHunter[1] ]
