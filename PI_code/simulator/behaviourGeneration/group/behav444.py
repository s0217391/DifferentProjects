#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + prey[1]
	temp1 = otherHunter[1] + otherHunter[1]
	temp2 = prey[0] - temp1
	if prey[0] != 0:
		temp3 = temp1 / prey[0]
	else:
		temp3 = prey[0]
	temp1 = min( prey[0] , temp3 )
	temp2 = temp2 * dist
	if dist != 0:
		temp2 = temp1 / dist
	else:
		temp2 = dist
	if temp1 != 0:
		temp0 = temp1 % temp1
	else:
		temp0 = temp1
	if prey[0] != 0:
		temp4 = temp3 / prey[0]
	else:
		temp4 = prey[0]
	temp5 = min( temp3 , dist )
	temp3 = -1 * otherHunter[1]
	temp5 = -1 * prey[1]
	if temp2 > temp3 :
		if otherHunter[1] != 0:
			temp2 = otherHunter[0] % otherHunter[1]
		else:
			temp2 = otherHunter[1]
	else:
		temp2 = temp3 - temp0
	if otherHunter[0] != 0:
		temp4 = otherHunter[0] % otherHunter[0]
	else:
		temp4 = otherHunter[0]
	temp3 = temp2 + temp4
	temp1 = temp4 - temp1
	temp5 = -1 * temp0
	temp6 = temp0 - temp5
	temp2 = min( otherHunter[0] , prey[1] )
	if otherHunter[1] != 0:
		temp5 = temp3 / otherHunter[1]
	else:
		temp5 = otherHunter[1]
	return [ otherHunter[0] , temp4 ]
