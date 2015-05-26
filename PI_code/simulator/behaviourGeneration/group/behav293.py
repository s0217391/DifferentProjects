#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = dist % dist
	else:
		temp0 = dist
	if temp0 != 0:
		temp1 = otherHunter[0] / temp0
	else:
		temp1 = temp0
	temp1 = prey[1] - otherHunter[1]
	temp1 = min( temp1 , prey[1] )
	if dist > prey[1] :
		temp1 = -1 * otherHunter[1]
	else:
		temp1 = otherHunter[1] * temp0
	temp0 = max( dist , prey[0] )
	if dist != 0:
		temp0 = temp0 / dist
	else:
		temp0 = dist
	temp2 = max( prey[0] , temp1 )
	temp3 = -1 * temp0
	temp1 = otherHunter[1] - prey[1]
	temp2 = max( otherHunter[0] , otherHunter[0] )
	temp2 = min( otherHunter[1] , prey[1] )
	temp4 = -1 * otherHunter[1]
	temp4 = dist * temp3
	if otherHunter[1] != 0:
		temp5 = otherHunter[0] % otherHunter[1]
	else:
		temp5 = otherHunter[1]
	temp1 = temp1 * temp1
	temp4 = otherHunter[0] - prey[1]
	if temp0 != 0:
		temp3 = prey[1] / temp0
	else:
		temp3 = temp0
	temp2 = min( temp2 , temp5 )
	if temp5 > otherHunter[1] :
		temp5 = temp0 - temp1
	else:
		if temp1 != 0:
			temp5 = temp4 / temp1
		else:
			temp5 = temp1
	return [ otherHunter[0] , temp3 ]
