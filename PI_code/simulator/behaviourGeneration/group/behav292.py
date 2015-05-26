#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = otherHunter[1] % dist
	else:
		temp0 = dist
	temp1 = max( prey[1] , prey[1] )
	if prey[1] > prey[1] :
		if temp1 > temp0 :
			temp2 = temp1 * prey[0]
		else:
			temp2 = otherHunter[1] * dist
	else:
		temp2 = prey[0] - otherHunter[0]
	temp1 = temp2 - prey[1]
	temp0 = max( temp2 , otherHunter[1] )
	temp3 = -1 * otherHunter[1]
	if temp0 > temp0 :
		temp4 = min( temp3 , prey[1] )
	else:
		temp4 = -1 * dist
	temp3 = max( prey[0] , temp1 )
	temp4 = dist * temp0
	if temp3 != 0:
		temp5 = temp1 / temp3
	else:
		temp5 = temp3
	temp0 = max( prey[1] , dist )
	temp0 = otherHunter[0] * otherHunter[0]
	if dist > prey[1] :
		temp5 = max( otherHunter[1] , temp3 )
	else:
		temp5 = dist - otherHunter[0]
	temp5 = temp2 - otherHunter[0]
	temp4 = -1 * prey[0]
	temp5 = prey[1] - prey[1]
	temp1 = temp4 + otherHunter[1]
	temp2 = temp2 + temp0
	return [ prey[1] , temp3 ]
