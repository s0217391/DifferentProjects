#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = prey[1] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = -1 * prey[1]
	temp1 = prey[0] - temp0
	if otherHunter[0] > otherHunter[0] :
		temp1 = -1 * temp0
	else:
		temp1 = max( otherHunter[1] , dist )
	temp2 = max( temp1 , otherHunter[0] )
	temp2 = max( temp1 , otherHunter[0] )
	if temp1 > dist :
		if otherHunter[1] != 0:
			temp0 = prey[0] / otherHunter[1]
		else:
			temp0 = otherHunter[1]
	else:
		temp0 = temp1 * otherHunter[0]
	temp1 = temp0 + dist
	temp1 = -1 * temp1
	if otherHunter[0] != 0:
		temp1 = temp2 / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if temp2 != 0:
		temp2 = temp1 % temp2
	else:
		temp2 = temp2
	temp1 = max( dist , prey[0] )
	temp1 = otherHunter[1] - temp0
	temp0 = -1 * temp0
	temp2 = temp2 + otherHunter[0]
	temp2 = prey[0] - prey[0]
	temp3 = max( temp2 , temp0 )
	temp4 = min( dist , temp2 )
	temp3 = max( temp1 , temp2 )
	temp4 = -1 * prey[1]
	temp4 = max( prey[1] , otherHunter[1] )
	temp5 = temp4 - temp4
	temp1 = -1 * temp0
	return [ otherHunter[0] , dist ]
