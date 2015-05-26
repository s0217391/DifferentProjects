#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] * otherHunter[1]
	if otherHunter[1] != 0:
		temp1 = prey[1] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp1 = max( temp1 , prey[0] )
	temp2 = min( temp1 , prey[1] )
	temp1 = -1 * prey[1]
	temp2 = max( otherHunter[0] , temp0 )
	temp2 = max( temp2 , dist )
	temp2 = max( temp2 , prey[0] )
	if temp1 != 0:
		temp1 = otherHunter[0] / temp1
	else:
		temp1 = temp1
	if temp1 != 0:
		temp0 = prey[0] / temp1
	else:
		temp0 = temp1
	temp2 = prey[0] + otherHunter[0]
	temp1 = max( temp2 , prey[1] )
	temp1 = otherHunter[1] - temp0
	if prey[1] != 0:
		temp0 = temp0 % prey[1]
	else:
		temp0 = prey[1]
	temp2 = max( prey[1] , prey[0] )
	if dist > prey[0] :
		if prey[0] != 0:
			temp1 = otherHunter[0] / prey[0]
		else:
			temp1 = prey[0]
	else:
		if temp2 != 0:
			temp1 = temp1 % temp2
		else:
			temp1 = temp2
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	temp1 = otherHunter[0] - otherHunter[1]
	temp3 = dist - prey[1]
	temp4 = temp0 - temp3
	temp5 = min( temp1 , prey[0] )
	temp3 = temp5 + temp4
	temp6 = -1 * temp5
	if temp4 > temp0 :
		temp2 = prey[1] + prey[0]
	else:
		temp2 = dist + temp5
	return [ temp4 , temp5 ]
