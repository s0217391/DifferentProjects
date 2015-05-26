#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * dist
	if dist > prey[1] :
		temp1 = -1 * otherHunter[0]
	else:
		if dist != 0:
			temp1 = otherHunter[0] / dist
		else:
			temp1 = dist
	temp0 = temp0 * prey[0]
	temp0 = min( temp0 , prey[1] )
	temp2 = min( dist , otherHunter[0] )
	temp0 = temp2 - prey[1]
	temp0 = temp2 - prey[1]
	temp3 = -1 * otherHunter[1]
	if dist != 0:
		temp1 = temp1 / dist
	else:
		temp1 = dist
	if temp0 != 0:
		temp4 = dist / temp0
	else:
		temp4 = temp0
	temp0 = temp2 + temp2
	if temp3 > prey[1] :
		temp3 = prey[0] * temp2
	else:
		if temp3 != 0:
			temp3 = prey[1] % temp3
		else:
			temp3 = temp3
	temp1 = max( temp0 , otherHunter[0] )
	temp0 = -1 * otherHunter[0]
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	if temp2 > temp3 :
		temp4 = max( prey[0] , temp0 )
	else:
		temp4 = max( dist , otherHunter[1] )
	if temp2 != 0:
		temp1 = otherHunter[1] / temp2
	else:
		temp1 = temp2
	temp3 = -1 * prey[0]
	temp5 = temp3 * dist
	return [ temp4 , temp3 ]
