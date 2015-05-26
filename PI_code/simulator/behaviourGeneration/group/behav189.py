#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist > otherHunter[1] :
		temp0 = min( prey[1] , prey[0] )
	else:
		if otherHunter[0] != 0:
			temp0 = prey[1] % otherHunter[0]
		else:
			temp0 = otherHunter[0]
	if prey[1] > temp0 :
		if temp0 != 0:
			temp1 = prey[1] / temp0
		else:
			temp1 = temp0
	else:
		temp1 = min( prey[1] , prey[0] )
	if temp0 != 0:
		temp0 = temp0 % temp0
	else:
		temp0 = temp0
	if prey[1] != 0:
		temp2 = dist % prey[1]
	else:
		temp2 = prey[1]
	temp2 = max( otherHunter[1] , temp2 )
	if dist != 0:
		temp3 = otherHunter[0] / dist
	else:
		temp3 = dist
	temp3 = -1 * prey[0]
	if otherHunter[1] != 0:
		temp3 = temp0 % otherHunter[1]
	else:
		temp3 = otherHunter[1]
	temp4 = -1 * temp2
	temp1 = max( temp3 , prey[1] )
	if temp0 != 0:
		temp3 = dist % temp0
	else:
		temp3 = temp0
	temp5 = max( temp2 , dist )
	temp0 = temp0 - temp1
	if dist != 0:
		temp6 = temp5 / dist
	else:
		temp6 = dist
	if temp4 > temp6 :
		if temp4 > prey[0] :
			if temp1 > temp2 :
				if temp5 > temp6 :
					temp6 = dist + temp0
				else:
					temp6 = min( temp0 , temp0 )
			else:
				temp6 = prey[1] - dist
		else:
			if temp0 != 0:
				temp6 = temp2 % temp0
			else:
				temp6 = temp0
	else:
		if temp4 > prey[1] :
			if temp1 != 0:
				temp6 = temp5 / temp1
			else:
				temp6 = temp1
		else:
			temp6 = temp5 * temp5
	if prey[0] != 0:
		temp4 = temp6 % prey[0]
	else:
		temp4 = prey[0]
	temp4 = max( otherHunter[0] , temp1 )
	if otherHunter[1] != 0:
		temp2 = temp4 / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	if temp1 != 0:
		temp0 = temp6 / temp1
	else:
		temp0 = temp1
	temp0 = max( otherHunter[1] , temp0 )
	if temp2 != 0:
		temp7 = dist % temp2
	else:
		temp7 = temp2
	return [ prey[1] , prey[0] ]
