#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[0]
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	temp2 = prey[0] * otherHunter[0]
	temp3 = max( prey[1] , prey[1] )
	temp1 = -1 * otherHunter[0]
	temp0 = max( temp2 , temp1 )
	if temp0 > temp3 :
		temp2 = dist + temp0
	else:
		if temp0 != 0:
			temp2 = otherHunter[1] / temp0
		else:
			temp2 = temp0
	temp1 = dist - prey[1]
	if temp3 != 0:
		temp2 = dist % temp3
	else:
		temp2 = temp3
	temp1 = temp1 * temp0
	if temp2 != 0:
		temp1 = dist % temp2
	else:
		temp1 = temp2
	temp0 = -1 * otherHunter[1]
	temp4 = min( temp1 , prey[0] )
	temp4 = -1 * temp1
	temp5 = -1 * temp1
	if temp3 != 0:
		temp3 = temp2 / temp3
	else:
		temp3 = temp3
	temp0 = min( temp4 , temp3 )
	if dist != 0:
		temp6 = temp1 / dist
	else:
		temp6 = dist
	temp5 = prey[1] + temp0
	temp7 = min( temp0 , otherHunter[0] )
	if temp6 != 0:
		temp3 = temp7 / temp6
	else:
		temp3 = temp6
	temp6 = otherHunter[1] * otherHunter[0]
	temp0 = temp1 - temp3
	return [ temp7 , dist ]
