#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist - prey[1]
	if prey[0] != 0:
		temp1 = otherHunter[1] % prey[0]
	else:
		temp1 = prey[0]
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	if temp1 > temp1 :
		if temp0 != 0:
			temp0 = prey[1] / temp0
		else:
			temp0 = temp0
	else:
		temp0 = max( dist , prey[1] )
	temp0 = max( otherHunter[0] , otherHunter[1] )
	temp0 = temp0 * prey[1]
	temp2 = temp1 * temp0
	if prey[1] != 0:
		temp0 = temp1 / prey[1]
	else:
		temp0 = prey[1]
	temp0 = -1 * prey[1]
	temp1 = prey[1] * otherHunter[0]
	temp3 = max( prey[0] , temp0 )
	if otherHunter[0] != 0:
		temp4 = prey[0] % otherHunter[0]
	else:
		temp4 = otherHunter[0]
	temp4 = max( temp1 , dist )
	if temp4 != 0:
		temp5 = temp4 / temp4
	else:
		temp5 = temp4
	temp0 = temp2 - dist
	temp5 = prey[0] * prey[1]
	temp5 = max( prey[0] , temp1 )
	if temp4 != 0:
		temp0 = prey[0] % temp4
	else:
		temp0 = temp4
	if temp3 != 0:
		temp3 = otherHunter[1] / temp3
	else:
		temp3 = temp3
	if temp3 != 0:
		temp3 = temp5 % temp3
	else:
		temp3 = temp3
	temp0 = temp0 * prey[1]
	if dist > temp5 :
		temp4 = temp0 + prey[1]
	else:
		if otherHunter[0] != 0:
			temp4 = temp3 / otherHunter[0]
		else:
			temp4 = otherHunter[0]
	temp6 = temp2 - otherHunter[0]
	return [ dist , otherHunter[0] ]
