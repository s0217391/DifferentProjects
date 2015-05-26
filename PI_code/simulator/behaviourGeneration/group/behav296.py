#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * prey[1]
	temp1 = prey[0] + prey[1]
	if temp0 != 0:
		temp2 = prey[1] % temp0
	else:
		temp2 = temp0
	temp1 = otherHunter[0] - prey[0]
	temp3 = temp1 * temp2
	if otherHunter[0] != 0:
		temp3 = dist / otherHunter[0]
	else:
		temp3 = otherHunter[0]
	if dist != 0:
		temp0 = dist % dist
	else:
		temp0 = dist
	temp1 = max( dist , temp1 )
	temp3 = prey[1] + prey[0]
	if prey[0] > temp3 :
		temp3 = max( temp0 , temp2 )
	else:
		temp3 = -1 * prey[0]
	temp4 = -1 * temp2
	temp5 = max( temp4 , otherHunter[0] )
	if temp1 > temp2 :
		temp3 = min( temp5 , otherHunter[0] )
	else:
		temp3 = prey[1] - temp3
	if otherHunter[0] > temp1 :
		if dist != 0:
			temp0 = prey[1] / dist
		else:
			temp0 = dist
	else:
		temp0 = otherHunter[1] + otherHunter[0]
	if dist != 0:
		temp5 = temp5 % dist
	else:
		temp5 = dist
	temp4 = max( temp2 , prey[0] )
	temp1 = -1 * otherHunter[0]
	if temp4 != 0:
		temp0 = temp1 % temp4
	else:
		temp0 = temp4
	temp6 = max( otherHunter[1] , temp3 )
	if otherHunter[1] != 0:
		temp2 = prey[1] / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp2 = otherHunter[1] + temp2
	temp7 = otherHunter[0] - temp6
	return [ temp3 , temp6 ]
