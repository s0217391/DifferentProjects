#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] - otherHunter[0]
	temp1 = dist - otherHunter[0]
	temp1 = min( prey[1] , temp1 )
	if temp0 > otherHunter[1] :
		temp1 = min( temp0 , prey[0] )
	else:
		temp1 = max( prey[1] , temp1 )
	temp0 = dist + temp1
	temp2 = max( temp0 , dist )
	temp2 = temp1 - prey[1]
	if otherHunter[0] != 0:
		temp1 = temp0 / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp3 = otherHunter[1] - otherHunter[1]
	if temp3 != 0:
		temp4 = temp3 / temp3
	else:
		temp4 = temp3
	temp4 = prey[0] - otherHunter[0]
	if temp0 > otherHunter[1] :
		if temp2 != 0:
			temp2 = temp4 % temp2
		else:
			temp2 = temp2
	else:
		temp2 = min( prey[1] , prey[1] )
	temp5 = prey[0] - temp2
	temp1 = -1 * temp3
	temp0 = temp2 + otherHunter[1]
	if dist != 0:
		temp4 = temp1 / dist
	else:
		temp4 = dist
	if otherHunter[1] != 0:
		temp2 = prey[1] / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp5 = max( temp1 , temp4 )
	temp0 = temp4 - temp5
	temp2 = max( otherHunter[0] , otherHunter[1] )
	temp0 = temp3 + temp4
	temp4 = max( otherHunter[1] , otherHunter[1] )
	return [ prey[0] , temp1 ]
