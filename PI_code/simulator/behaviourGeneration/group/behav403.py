#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] + otherHunter[0]
	temp1 = min( temp0 , dist )
	temp1 = max( temp0 , otherHunter[1] )
	if prey[1] != 0:
		temp2 = prey[1] % prey[1]
	else:
		temp2 = prey[1]
	temp1 = -1 * temp0
	temp2 = temp0 * otherHunter[0]
	if dist > temp1 :
		temp2 = prey[1] * prey[1]
	else:
		if otherHunter[0] != 0:
			temp2 = temp1 % otherHunter[0]
		else:
			temp2 = otherHunter[0]
	temp3 = temp1 - prey[0]
	if temp0 != 0:
		temp4 = prey[0] / temp0
	else:
		temp4 = temp0
	temp0 = dist - temp0
	if otherHunter[1] != 0:
		temp4 = prey[0] / otherHunter[1]
	else:
		temp4 = otherHunter[1]
	temp5 = min( temp2 , otherHunter[0] )
	temp1 = temp2 + dist
	temp5 = temp4 * temp4
	if prey[1] > prey[0] :
		temp3 = max( temp3 , temp1 )
	else:
		if temp0 != 0:
			temp3 = temp1 / temp0
		else:
			temp3 = temp0
	temp1 = otherHunter[0] * temp5
	temp5 = -1 * otherHunter[0]
	temp1 = temp2 * dist
	if prey[1] != 0:
		temp1 = temp1 / prey[1]
	else:
		temp1 = prey[1]
	temp6 = max( temp5 , otherHunter[1] )
	if temp2 > temp0 :
		if temp4 != 0:
			temp5 = temp0 % temp4
		else:
			temp5 = temp4
	else:
		temp5 = max( otherHunter[0] , otherHunter[1] )
	return [ temp2 , temp2 ]
