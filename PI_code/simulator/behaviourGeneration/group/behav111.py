#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , prey[1] )
	temp1 = max( otherHunter[0] , prey[0] )
	temp2 = -1 * dist
	temp2 = min( temp0 , otherHunter[0] )
	temp2 = -1 * temp1
	temp1 = -1 * temp2
	temp0 = min( otherHunter[1] , otherHunter[1] )
	temp1 = temp2 - temp1
	temp0 = otherHunter[1] * otherHunter[1]
	if dist != 0:
		temp1 = temp2 / dist
	else:
		temp1 = dist
	if prey[0] > otherHunter[1] :
		temp1 = temp2 - temp2
	else:
		temp1 = dist - prey[1]
	if prey[0] != 0:
		temp2 = prey[1] % prey[0]
	else:
		temp2 = prey[0]
	temp2 = prey[0] + prey[1]
	temp0 = prey[0] - temp1
	temp0 = min( otherHunter[1] , temp0 )
	temp2 = temp2 * temp2
	if temp0 > prey[1] :
		temp3 = min( prey[1] , prey[1] )
	else:
		temp3 = temp0 + temp0
	temp3 = temp0 - temp0
	temp0 = temp2 + prey[1]
	if prey[1] != 0:
		temp0 = otherHunter[0] % prey[1]
	else:
		temp0 = prey[1]
	if dist != 0:
		temp2 = temp2 % dist
	else:
		temp2 = dist
	temp4 = -1 * otherHunter[1]
	if temp1 > prey[1] :
		temp5 = temp0 - otherHunter[0]
	else:
		if temp4 != 0:
			temp5 = prey[0] / temp4
		else:
			temp5 = temp4
	temp2 = max( temp1 , otherHunter[1] )
	return [ dist , temp0 ]
