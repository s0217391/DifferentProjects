#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , prey[1] )
	temp1 = dist - prey[0]
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp0 = max( otherHunter[0] , prey[0] )
	temp0 = otherHunter[1] - prey[1]
	if prey[0] > dist :
		if temp0 != 0:
			temp2 = prey[1] % temp0
		else:
			temp2 = temp0
	else:
		temp2 = temp0 - otherHunter[0]
	temp0 = max( prey[0] , prey[1] )
	temp3 = temp0 + temp2
	temp1 = min( otherHunter[1] , temp1 )
	temp2 = otherHunter[0] - dist
	temp4 = -1 * temp1
	if temp2 != 0:
		temp4 = temp4 % temp2
	else:
		temp4 = temp2
	if temp4 != 0:
		temp4 = prey[0] % temp4
	else:
		temp4 = temp4
	temp3 = dist * otherHunter[1]
	temp1 = max( otherHunter[1] , dist )
	temp4 = temp4 + otherHunter[0]
	if prey[1] != 0:
		temp5 = temp2 % prey[1]
	else:
		temp5 = prey[1]
	return [ prey[0] , temp4 ]
