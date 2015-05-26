#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist - prey[1]
	if dist != 0:
		temp1 = temp0 / dist
	else:
		temp1 = dist
	if prey[1] != 0:
		temp0 = otherHunter[0] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = temp1 * prey[1]
	if temp0 > prey[1] :
		temp0 = max( prey[1] , prey[1] )
	else:
		if dist > prey[1] :
			if temp1 != 0:
				temp0 = temp0 % temp1
			else:
				temp0 = temp1
		else:
			temp0 = min( temp0 , prey[0] )
	temp2 = dist - otherHunter[0]
	temp0 = dist - temp2
	if temp2 != 0:
		temp3 = otherHunter[1] / temp2
	else:
		temp3 = temp2
	temp2 = temp3 + prey[1]
	temp3 = prey[1] + prey[0]
	if prey[1] > temp1 :
		temp3 = prey[1] - otherHunter[1]
	else:
		if otherHunter[1] > otherHunter[1] :
			if prey[1] != 0:
				temp3 = dist % prey[1]
			else:
				temp3 = prey[1]
		else:
			temp3 = min( temp3 , prey[1] )
	if temp2 != 0:
		temp3 = dist / temp2
	else:
		temp3 = temp2
	temp2 = prey[1] * temp2
	if temp3 != 0:
		temp1 = temp0 % temp3
	else:
		temp1 = temp3
	temp1 = -1 * otherHunter[0]
	temp4 = min( prey[1] , dist )
	if temp0 != 0:
		temp0 = temp0 / temp0
	else:
		temp0 = temp0
	temp4 = temp4 + temp3
	temp1 = -1 * dist
	return [ prey[1] , dist ]
