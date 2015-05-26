#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = dist % dist
	else:
		temp0 = dist
	temp1 = temp0 + temp0
	temp0 = max( otherHunter[1] , prey[0] )
	temp0 = temp0 * temp0
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp0 = -1 * otherHunter[0]
	temp2 = max( prey[1] , dist )
	temp3 = -1 * otherHunter[0]
	temp0 = prey[0] - otherHunter[0]
	temp3 = min( temp2 , otherHunter[0] )
	if temp3 != 0:
		temp2 = temp1 % temp3
	else:
		temp2 = temp3
	temp4 = prey[0] + otherHunter[1]
	temp0 = temp4 - prey[1]
	temp5 = min( temp0 , prey[1] )
	if prey[0] > prey[1] :
		temp5 = min( temp5 , temp5 )
	else:
		temp5 = max( otherHunter[1] , prey[0] )
	if prey[1] != 0:
		temp1 = temp5 % prey[1]
	else:
		temp1 = prey[1]
	temp3 = min( temp1 , temp0 )
	return [ prey[0] , prey[0] ]
