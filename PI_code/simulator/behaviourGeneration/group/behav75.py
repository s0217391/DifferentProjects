#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[0] , dist )
	temp1 = -1 * otherHunter[0]
	temp1 = -1 * otherHunter[0]
	temp1 = otherHunter[1] + prey[0]
	temp2 = min( temp1 , prey[0] )
	if dist > temp0 :
		temp3 = min( temp0 , prey[0] )
	else:
		if otherHunter[1] != 0:
			temp3 = dist % otherHunter[1]
		else:
			temp3 = otherHunter[1]
	temp3 = min( temp0 , temp3 )
	if prey[1] > temp0 :
		temp0 = otherHunter[0] * otherHunter[0]
	else:
		temp0 = min( temp0 , dist )
	if temp1 != 0:
		temp2 = temp2 % temp1
	else:
		temp2 = temp1
	temp0 = max( temp2 , prey[1] )
	if temp0 > temp3 :
		temp3 = temp1 * temp3
	else:
		if temp0 > temp3 :
			if temp2 != 0:
				temp3 = dist / temp2
			else:
				temp3 = temp2
		else:
			if temp0 != 0:
				temp3 = temp0 % temp0
			else:
				temp3 = temp0
	temp4 = -1 * temp1
	if temp0 != 0:
		temp5 = prey[1] % temp0
	else:
		temp5 = temp0
	temp4 = temp5 - otherHunter[0]
	temp1 = otherHunter[0] + temp1
	if temp4 != 0:
		temp6 = dist % temp4
	else:
		temp6 = temp4
	temp5 = -1 * otherHunter[1]
	if dist != 0:
		temp2 = otherHunter[0] % dist
	else:
		temp2 = dist
	if temp5 > temp3 :
		temp6 = min( temp3 , temp2 )
	else:
		temp6 = max( temp3 , dist )
	temp7 = temp5 - temp3
	if temp3 != 0:
		temp8 = temp0 / temp3
	else:
		temp8 = temp3
	if temp3 > temp3 :
		temp6 = otherHunter[0] + otherHunter[0]
	else:
		temp6 = temp6 * temp8
	return [ temp7 , prey[0] ]
