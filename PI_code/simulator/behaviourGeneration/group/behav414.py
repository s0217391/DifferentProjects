#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	if dist != 0:
		temp1 = otherHunter[1] / dist
	else:
		temp1 = dist
	if otherHunter[1] > prey[1] :
		temp0 = otherHunter[0] * prey[1]
	else:
		temp0 = temp1 + otherHunter[0]
	if prey[0] != 0:
		temp0 = otherHunter[0] % prey[0]
	else:
		temp0 = prey[0]
	temp2 = -1 * otherHunter[1]
	if otherHunter[1] != 0:
		temp3 = dist % otherHunter[1]
	else:
		temp3 = otherHunter[1]
	if otherHunter[0] > temp1 :
		temp2 = max( otherHunter[1] , temp2 )
	else:
		if otherHunter[0] != 0:
			temp2 = temp1 / otherHunter[0]
		else:
			temp2 = otherHunter[0]
	if otherHunter[1] != 0:
		temp3 = temp3 % otherHunter[1]
	else:
		temp3 = otherHunter[1]
	temp4 = -1 * temp3
	temp4 = otherHunter[0] * temp2
	temp4 = temp2 + prey[1]
	temp3 = -1 * temp1
	temp2 = -1 * temp1
	temp5 = temp3 - temp3
	temp2 = -1 * temp2
	temp2 = max( temp5 , dist )
	temp4 = temp0 - temp5
	temp5 = -1 * otherHunter[0]
	if otherHunter[1] != 0:
		temp1 = dist / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp1 = min( otherHunter[1] , otherHunter[1] )
	if temp3 > temp4 :
		temp1 = min( prey[1] , temp5 )
	else:
		temp1 = temp0 * otherHunter[1]
	return [ temp3 , temp3 ]
