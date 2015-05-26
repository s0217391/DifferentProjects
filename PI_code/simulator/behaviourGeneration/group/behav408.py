#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] + otherHunter[0]
	if prey[0] != 0:
		temp1 = dist % prey[0]
	else:
		temp1 = prey[0]
	temp2 = -1 * otherHunter[1]
	temp0 = temp1 - prey[1]
	if prey[1] > otherHunter[0] :
		if dist > prey[1] :
			temp2 = temp1 * prey[1]
		else:
			temp2 = otherHunter[0] - temp1
	else:
		temp2 = dist + otherHunter[0]
	temp0 = temp2 * otherHunter[0]
	temp2 = min( otherHunter[1] , temp2 )
	if prey[0] != 0:
		temp1 = temp2 % prey[0]
	else:
		temp1 = prey[0]
	temp0 = dist - temp0
	temp1 = -1 * dist
	temp0 = temp0 + temp1
	temp1 = prey[1] + otherHunter[1]
	temp1 = min( dist , prey[1] )
	temp2 = prey[1] * dist
	if temp2 != 0:
		temp2 = dist % temp2
	else:
		temp2 = temp2
	temp0 = otherHunter[1] + temp1
	temp3 = min( temp1 , dist )
	temp1 = max( otherHunter[1] , temp3 )
	return [ otherHunter[0] , dist ]
