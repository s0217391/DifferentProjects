#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] - prey[0]
	temp1 = max( temp0 , dist )
	temp2 = otherHunter[1] - otherHunter[1]
	temp2 = max( prey[1] , temp1 )
	temp2 = otherHunter[0] - dist
	temp3 = -1 * temp1
	temp4 = min( temp1 , otherHunter[0] )
	if temp4 != 0:
		temp2 = temp1 / temp4
	else:
		temp2 = temp4
	if temp3 != 0:
		temp4 = temp4 % temp3
	else:
		temp4 = temp3
	temp1 = min( temp2 , temp3 )
	temp0 = -1 * otherHunter[1]
	if otherHunter[1] > temp2 :
		if prey[0] != 0:
			temp0 = temp3 / prey[0]
		else:
			temp0 = prey[0]
	else:
		temp0 = -1 * temp3
	if otherHunter[0] != 0:
		temp5 = otherHunter[0] / otherHunter[0]
	else:
		temp5 = otherHunter[0]
	temp3 = max( prey[1] , temp3 )
	if temp5 != 0:
		temp4 = otherHunter[0] / temp5
	else:
		temp4 = temp5
	return [ otherHunter[1] , temp0 ]
