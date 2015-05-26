#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > otherHunter[1] :
		if prey[0] > prey[0] :
			if otherHunter[1] != 0:
				temp0 = otherHunter[0] / otherHunter[1]
			else:
				temp0 = otherHunter[1]
		else:
			temp0 = min( otherHunter[1] , otherHunter[0] )
	else:
		temp0 = max( prey[1] , otherHunter[0] )
	temp1 = prey[1] + dist
	temp1 = -1 * temp1
	if dist > otherHunter[1] :
		if temp1 != 0:
			temp0 = otherHunter[1] / temp1
		else:
			temp0 = temp1
	else:
		temp0 = dist + prey[1]
	temp0 = prey[0] - temp0
	if otherHunter[1] != 0:
		temp1 = temp0 % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if temp1 > temp0 :
		temp0 = max( temp0 , prey[0] )
	else:
		temp0 = -1 * otherHunter[1]
	temp1 = dist + dist
	if dist != 0:
		temp0 = prey[0] / dist
	else:
		temp0 = dist
	temp2 = prey[0] - otherHunter[0]
	temp0 = prey[1] * temp1
	temp0 = max( dist , prey[1] )
	temp1 = dist + dist
	temp3 = max( prey[1] , temp1 )
	temp3 = temp1 * prey[1]
	temp4 = max( temp0 , prey[0] )
	if prey[1] > temp2 :
		temp2 = dist * temp1
	else:
		temp2 = temp3 - dist
	temp4 = dist + otherHunter[1]
	temp2 = -1 * temp4
	temp3 = prey[1] * prey[1]
	temp5 = otherHunter[0] * otherHunter[0]
	if temp1 > otherHunter[0] :
		temp5 = prey[0] + prey[1]
	else:
		temp5 = temp4 * otherHunter[0]
	temp2 = prey[0] + temp5
	if dist != 0:
		temp2 = temp2 / dist
	else:
		temp2 = dist
	temp5 = -1 * temp5
	return [ temp0 , temp5 ]
