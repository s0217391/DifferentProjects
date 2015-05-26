#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = prey[0] + temp0
	temp0 = otherHunter[0] + prey[0]
	temp2 = max( dist , dist )
	temp0 = dist - prey[0]
	temp0 = otherHunter[0] + temp1
	if temp1 != 0:
		temp3 = otherHunter[1] / temp1
	else:
		temp3 = temp1
	if otherHunter[1] != 0:
		temp4 = temp3 / otherHunter[1]
	else:
		temp4 = otherHunter[1]
	temp2 = prey[0] - dist
	temp2 = temp1 + temp0
	temp1 = max( temp0 , temp1 )
	temp5 = max( temp2 , otherHunter[0] )
	temp0 = otherHunter[0] - prey[1]
	if prey[1] > temp5 :
		temp5 = max( temp5 , temp3 )
	else:
		temp5 = temp3 + otherHunter[0]
	temp0 = max( temp2 , otherHunter[1] )
	if temp5 > temp3 :
		temp6 = temp2 * otherHunter[1]
	else:
		if otherHunter[0] != 0:
			temp6 = temp2 / otherHunter[0]
		else:
			temp6 = otherHunter[0]
	temp4 = temp5 - prey[0]
	return [ dist , dist ]
