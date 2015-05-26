#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = otherHunter[0] % prey[1]
	else:
		temp0 = prey[1]
	if otherHunter[0] != 0:
		temp1 = temp0 / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if temp1 != 0:
		temp2 = otherHunter[1] / temp1
	else:
		temp2 = temp1
	temp2 = prey[0] - prey[1]
	temp2 = -1 * temp0
	if dist != 0:
		temp3 = prey[1] / dist
	else:
		temp3 = dist
	temp3 = max( temp1 , prey[1] )
	temp0 = prey[1] * temp2
	temp4 = -1 * temp2
	temp1 = min( otherHunter[1] , temp1 )
	if temp0 != 0:
		temp2 = temp0 % temp0
	else:
		temp2 = temp0
	temp5 = max( temp0 , temp2 )
	temp5 = temp0 * temp0
	temp1 = min( prey[0] , temp3 )
	temp4 = dist + temp4
	if prey[1] != 0:
		temp6 = otherHunter[0] % prey[1]
	else:
		temp6 = prey[1]
	temp0 = prey[1] * temp1
	if temp0 > temp3 :
		if prey[0] > temp3 :
			temp4 = -1 * prey[0]
		else:
			temp4 = min( otherHunter[0] , temp0 )
	else:
		if otherHunter[0] != 0:
			temp4 = dist / otherHunter[0]
		else:
			temp4 = otherHunter[0]
	if otherHunter[1] != 0:
		temp7 = temp5 / otherHunter[1]
	else:
		temp7 = otherHunter[1]
	temp6 = dist - temp3
	temp3 = prey[1] * prey[0]
	temp2 = temp2 - temp7
	if dist != 0:
		temp3 = temp1 % dist
	else:
		temp3 = dist
	return [ prey[0] , temp1 ]
