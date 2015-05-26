#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = otherHunter[1] / dist
	else:
		temp0 = dist
	temp1 = otherHunter[1] - otherHunter[1]
	temp2 = prey[1] - otherHunter[0]
	if prey[1] > temp0 :
		temp2 = temp0 * prey[1]
	else:
		temp2 = otherHunter[0] - temp2
	temp3 = max( temp0 , temp1 )
	if otherHunter[1] != 0:
		temp3 = prey[0] % otherHunter[1]
	else:
		temp3 = otherHunter[1]
	if prey[1] != 0:
		temp1 = temp2 / prey[1]
	else:
		temp1 = prey[1]
	if dist > otherHunter[0] :
		temp0 = max( temp0 , otherHunter[0] )
	else:
		if dist != 0:
			temp0 = otherHunter[0] / dist
		else:
			temp0 = dist
	temp4 = -1 * prey[0]
	if temp0 != 0:
		temp2 = temp4 % temp0
	else:
		temp2 = temp0
	temp1 = prey[1] + dist
	if prey[0] != 0:
		temp5 = temp0 % prey[0]
	else:
		temp5 = prey[0]
	temp6 = temp2 * otherHunter[1]
	if otherHunter[1] > prey[1] :
		temp3 = temp2 - dist
	else:
		temp3 = max( otherHunter[1] , otherHunter[1] )
	temp4 = otherHunter[0] * temp6
	if temp3 != 0:
		temp7 = prey[0] % temp3
	else:
		temp7 = temp3
	return [ prey[1] , temp7 ]
