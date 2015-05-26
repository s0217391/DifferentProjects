#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] > otherHunter[1] :
		temp0 = -1 * prey[0]
	else:
		if prey[0] > prey[0] :
			temp0 = -1 * prey[1]
		else:
			temp0 = otherHunter[1] - otherHunter[1]
	temp1 = min( dist , prey[0] )
	temp2 = min( otherHunter[0] , dist )
	temp0 = dist + otherHunter[0]
	if prey[0] > prey[0] :
		if otherHunter[0] != 0:
			temp2 = temp0 % otherHunter[0]
		else:
			temp2 = otherHunter[0]
	else:
		temp2 = -1 * temp2
	temp2 = min( temp1 , dist )
	temp3 = min( prey[1] , temp1 )
	if prey[1] != 0:
		temp3 = otherHunter[1] % prey[1]
	else:
		temp3 = prey[1]
	if temp3 != 0:
		temp1 = otherHunter[0] % temp3
	else:
		temp1 = temp3
	temp0 = otherHunter[0] - prey[1]
	if temp2 != 0:
		temp4 = temp0 / temp2
	else:
		temp4 = temp2
	temp0 = min( temp1 , temp4 )
	return [ temp3 , temp4 ]
