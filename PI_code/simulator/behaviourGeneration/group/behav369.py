#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = otherHunter[1] / dist
	else:
		temp0 = dist
	if temp0 != 0:
		temp1 = otherHunter[0] / temp0
	else:
		temp1 = temp0
	if temp0 != 0:
		temp2 = otherHunter[1] % temp0
	else:
		temp2 = temp0
	temp3 = dist * prey[1]
	temp4 = min( prey[0] , dist )
	if temp0 != 0:
		temp5 = temp0 % temp0
	else:
		temp5 = temp0
	if otherHunter[1] != 0:
		temp2 = otherHunter[0] / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	if temp0 > temp1 :
		if prey[1] > temp0 :
			if temp3 != 0:
				temp0 = temp1 % temp3
			else:
				temp0 = temp3
		else:
			if temp1 != 0:
				temp0 = dist / temp1
			else:
				temp0 = temp1
	else:
		temp0 = otherHunter[0] + temp4
	temp4 = otherHunter[1] * prey[1]
	if otherHunter[0] > prey[1] :
		if prey[0] != 0:
			temp2 = prey[0] % prey[0]
		else:
			temp2 = prey[0]
	else:
		temp2 = temp3 * temp2
	temp2 = max( temp0 , otherHunter[1] )
	temp6 = otherHunter[1] + temp5
	temp1 = max( temp4 , temp0 )
	temp4 = max( prey[1] , temp0 )
	temp7 = prey[1] - otherHunter[0]
	temp0 = min( temp6 , temp3 )
	temp4 = prey[1] * temp2
	temp5 = temp0 * temp7
	temp7 = prey[0] - otherHunter[1]
	if temp3 > temp3 :
		temp1 = min( temp1 , temp2 )
	else:
		temp1 = temp0 - temp5
	temp0 = prey[1] * temp3
	temp6 = otherHunter[0] * otherHunter[0]
	temp6 = max( temp4 , temp5 )
	return [ temp3 , temp6 ]
