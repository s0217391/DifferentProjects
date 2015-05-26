#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[0]
	if otherHunter[1] != 0:
		temp1 = prey[1] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp1 = dist - prey[0]
	temp1 = max( otherHunter[0] , temp0 )
	if temp1 != 0:
		temp1 = temp0 / temp1
	else:
		temp1 = temp1
	if otherHunter[0] != 0:
		temp1 = otherHunter[1] / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if dist != 0:
		temp2 = prey[1] / dist
	else:
		temp2 = dist
	if prey[0] > prey[0] :
		temp1 = otherHunter[0] * temp1
	else:
		temp1 = otherHunter[0] * temp1
	if temp1 > dist :
		temp0 = -1 * temp2
	else:
		temp0 = prey[0] - prey[0]
	if temp1 != 0:
		temp3 = dist % temp1
	else:
		temp3 = temp1
	if temp3 != 0:
		temp4 = prey[1] % temp3
	else:
		temp4 = temp3
	temp0 = max( temp4 , otherHunter[0] )
	temp0 = max( temp0 , otherHunter[0] )
	temp2 = -1 * otherHunter[1]
	if temp1 > temp1 :
		if otherHunter[0] > dist :
			if temp0 != 0:
				temp5 = prey[1] % temp0
			else:
				temp5 = temp0
		else:
			if temp0 != 0:
				temp5 = otherHunter[0] / temp0
			else:
				temp5 = temp0
	else:
		temp5 = -1 * temp0
	temp3 = temp2 * temp0
	temp0 = min( prey[1] , otherHunter[0] )
	temp4 = temp2 - dist
	if temp1 != 0:
		temp3 = otherHunter[1] % temp1
	else:
		temp3 = temp1
	temp6 = temp3 + temp4
	if otherHunter[1] != 0:
		temp5 = otherHunter[1] / otherHunter[1]
	else:
		temp5 = otherHunter[1]
	temp7 = min( temp0 , temp0 )
	temp4 = otherHunter[1] * prey[1]
	temp7 = max( temp1 , temp2 )
	return [ temp6 , temp6 ]
