#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] - dist
	temp1 = max( dist , otherHunter[0] )
	temp1 = temp1 - temp1
	if otherHunter[1] != 0:
		temp0 = otherHunter[1] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = max( prey[0] , otherHunter[1] )
	temp2 = -1 * dist
	temp0 = temp2 * temp1
	if prey[1] > otherHunter[1] :
		temp2 = max( dist , temp1 )
	else:
		temp2 = temp1 * dist
	temp1 = dist * temp2
	temp0 = -1 * temp0
	if prey[0] != 0:
		temp0 = otherHunter[1] / prey[0]
	else:
		temp0 = prey[0]
	temp2 = prey[1] + temp0
	if otherHunter[1] > temp1 :
		if temp1 > otherHunter[0] :
			temp2 = -1 * otherHunter[0]
		else:
			if temp0 != 0:
				temp2 = dist / temp0
			else:
				temp2 = temp0
	else:
		temp2 = temp0 * temp2
	temp1 = temp0 * prey[0]
	temp3 = min( temp2 , prey[0] )
	temp0 = prey[0] * temp0
	if temp0 > prey[1] :
		temp2 = -1 * otherHunter[0]
	else:
		if prey[1] != 0:
			temp2 = temp3 / prey[1]
		else:
			temp2 = prey[1]
	temp4 = -1 * otherHunter[1]
	if temp4 != 0:
		temp1 = temp2 % temp4
	else:
		temp1 = temp4
	temp5 = temp4 + temp2
	temp4 = temp3 - temp3
	if otherHunter[0] > prey[1] :
		temp2 = -1 * temp1
	else:
		temp2 = temp3 * prey[0]
	if temp0 != 0:
		temp0 = temp2 / temp0
	else:
		temp0 = temp0
	return [ otherHunter[1] , otherHunter[1] ]
