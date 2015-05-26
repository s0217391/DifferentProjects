#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	if temp0 != 0:
		temp1 = prey[1] % temp0
	else:
		temp1 = temp0
	temp0 = prey[1] * temp1
	temp2 = prey[1] * prey[1]
	temp3 = otherHunter[1] * prey[1]
	if temp2 != 0:
		temp0 = prey[1] / temp2
	else:
		temp0 = temp2
	if temp2 != 0:
		temp3 = temp1 / temp2
	else:
		temp3 = temp2
	if prey[1] != 0:
		temp3 = temp1 % prey[1]
	else:
		temp3 = prey[1]
	temp3 = max( otherHunter[1] , temp2 )
	temp0 = -1 * prey[0]
	temp3 = -1 * otherHunter[0]
	if temp1 != 0:
		temp4 = temp1 % temp1
	else:
		temp4 = temp1
	temp5 = temp3 + prey[1]
	if temp3 > temp1 :
		temp1 = min( temp1 , otherHunter[0] )
	else:
		if otherHunter[0] > otherHunter[0] :
			temp1 = temp1 * temp0
		else:
			temp1 = max( temp2 , otherHunter[1] )
	temp1 = max( temp5 , temp4 )
	if dist != 0:
		temp2 = temp5 % dist
	else:
		temp2 = dist
	temp1 = min( temp3 , temp4 )
	return [ otherHunter[0] , temp2 ]
