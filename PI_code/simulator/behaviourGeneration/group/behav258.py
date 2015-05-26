#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist + otherHunter[0]
	if otherHunter[1] > prey[1] :
		if temp0 != 0:
			temp1 = dist % temp0
		else:
			temp1 = temp0
	else:
		temp1 = dist + prey[0]
	temp0 = min( temp1 , temp0 )
	temp2 = prey[0] * dist
	temp2 = prey[0] - otherHunter[1]
	temp2 = min( temp1 , temp0 )
	temp3 = prey[1] - temp1
	if otherHunter[0] != 0:
		temp0 = temp3 % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp3 = temp0 * temp2
	temp3 = prey[0] * temp1
	return [ prey[1] , dist ]
