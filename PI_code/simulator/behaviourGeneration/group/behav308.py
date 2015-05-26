#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] * otherHunter[0]
	temp1 = min( prey[1] , prey[1] )
	if temp1 != 0:
		temp2 = temp1 % temp1
	else:
		temp2 = temp1
	temp0 = min( prey[1] , dist )
	temp3 = prey[0] * temp2
	if temp0 > temp1 :
		temp0 = prey[1] - temp3
	else:
		temp0 = otherHunter[1] * temp3
	temp1 = dist + otherHunter[0]
	temp2 = -1 * prey[1]
	temp3 = temp1 + prey[0]
	temp4 = temp3 - temp3
	temp0 = max( temp2 , otherHunter[1] )
	temp5 = -1 * dist
	temp1 = otherHunter[1] - temp3
	if temp4 != 0:
		temp0 = temp2 % temp4
	else:
		temp0 = temp4
	temp3 = otherHunter[1] + temp2
	if otherHunter[0] > temp1 :
		temp4 = max( prey[0] , temp1 )
	else:
		temp4 = temp1 * temp0
	if otherHunter[0] != 0:
		temp4 = temp5 / otherHunter[0]
	else:
		temp4 = otherHunter[0]
	return [ prey[0] , temp5 ]
