#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] - prey[1]
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	temp1 = prey[1] - temp0
	temp0 = dist + prey[1]
	temp0 = min( temp0 , dist )
	if prey[0] != 0:
		temp2 = prey[1] / prey[0]
	else:
		temp2 = prey[0]
	if otherHunter[0] > otherHunter[0] :
		temp1 = prey[1] * prey[0]
	else:
		temp1 = temp1 * otherHunter[0]
	temp3 = min( prey[0] , temp0 )
	temp2 = min( temp1 , temp0 )
	if prey[1] > otherHunter[0] :
		if temp1 > dist :
			temp3 = -1 * otherHunter[1]
		else:
			if temp3 != 0:
				temp3 = prey[0] / temp3
			else:
				temp3 = temp3
	else:
		temp3 = otherHunter[1] + prey[0]
	if dist > prey[0] :
		temp0 = max( dist , temp1 )
	else:
		if temp0 > otherHunter[0] :
			temp0 = prey[0] + otherHunter[1]
		else:
			temp0 = otherHunter[0] * temp0
	temp4 = temp2 * temp0
	temp5 = -1 * otherHunter[0]
	if temp5 > prey[0] :
		if temp4 != 0:
			temp2 = otherHunter[1] / temp4
		else:
			temp2 = temp4
	else:
		if prey[1] != 0:
			temp2 = prey[1] / prey[1]
		else:
			temp2 = prey[1]
	if temp2 != 0:
		temp2 = temp2 % temp2
	else:
		temp2 = temp2
	return [ temp0 , prey[0] ]
