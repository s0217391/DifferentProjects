#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] > prey[0] :
		if dist != 0:
			temp0 = otherHunter[1] / dist
		else:
			temp0 = dist
	else:
		temp0 = min( otherHunter[0] , dist )
	if otherHunter[1] != 0:
		temp1 = dist % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if otherHunter[0] != 0:
		temp1 = dist / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp2 = max( temp0 , temp1 )
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	temp2 = -1 * temp0
	temp2 = min( otherHunter[1] , temp0 )
	temp3 = max( temp1 , prey[0] )
	if dist != 0:
		temp2 = otherHunter[1] / dist
	else:
		temp2 = dist
	if temp3 != 0:
		temp3 = prey[1] / temp3
	else:
		temp3 = temp3
	temp0 = temp1 + otherHunter[0]
	temp4 = temp3 + temp3
	return [ temp3 , temp2 ]
