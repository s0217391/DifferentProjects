#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] * prey[1]
	temp1 = dist - prey[1]
	temp0 = max( prey[0] , otherHunter[1] )
	temp0 = otherHunter[1] - prey[0]
	temp2 = dist * otherHunter[0]
	temp2 = min( prey[0] , dist )
	if temp2 != 0:
		temp1 = otherHunter[1] / temp2
	else:
		temp1 = temp2
	temp0 = prey[1] - temp2
	if otherHunter[1] != 0:
		temp2 = temp1 % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp0 = min( prey[1] , temp1 )
	if temp1 > temp2 :
		if otherHunter[1] != 0:
			temp2 = temp2 / otherHunter[1]
		else:
			temp2 = otherHunter[1]
	else:
		if temp1 != 0:
			temp2 = dist % temp1
		else:
			temp2 = temp1
	temp3 = otherHunter[1] * otherHunter[0]
	if temp2 > temp1 :
		if dist != 0:
			temp1 = dist % dist
		else:
			temp1 = dist
	else:
		if temp1 > temp0 :
			if prey[0] > otherHunter[1] :
				temp1 = prey[1] * otherHunter[1]
			else:
				temp1 = dist - prey[1]
		else:
			if temp0 != 0:
				temp1 = prey[0] / temp0
			else:
				temp1 = temp0
	if temp3 != 0:
		temp4 = temp2 % temp3
	else:
		temp4 = temp3
	temp4 = otherHunter[1] - temp0
	temp0 = min( temp0 , dist )
	temp4 = otherHunter[1] * otherHunter[1]
	temp3 = -1 * prey[1]
	temp2 = -1 * temp0
	if prey[0] != 0:
		temp0 = temp1 % prey[0]
	else:
		temp0 = prey[0]
	return [ otherHunter[1] , temp3 ]
