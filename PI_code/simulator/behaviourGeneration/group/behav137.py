#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , prey[0] )
	if temp0 != 0:
		temp1 = prey[0] / temp0
	else:
		temp1 = temp0
	temp0 = -1 * dist
	if prey[0] > prey[1] :
		if temp0 != 0:
			temp1 = temp1 % temp0
		else:
			temp1 = temp0
	else:
		temp1 = -1 * prey[1]
	if temp0 > prey[1] :
		if otherHunter[1] != 0:
			temp0 = prey[0] / otherHunter[1]
		else:
			temp0 = otherHunter[1]
	else:
		temp0 = max( prey[1] , temp0 )
	temp2 = prey[0] - dist
	temp3 = otherHunter[1] * prey[1]
	if prey[1] > temp3 :
		temp1 = dist - dist
	else:
		temp1 = min( dist , temp2 )
	if dist > temp2 :
		if dist != 0:
			temp4 = temp0 / dist
		else:
			temp4 = dist
	else:
		temp4 = otherHunter[1] - temp0
	temp5 = temp1 * otherHunter[0]
	temp2 = -1 * temp0
	temp5 = max( prey[0] , otherHunter[0] )
	temp4 = otherHunter[1] + temp4
	temp3 = -1 * temp3
	if temp3 != 0:
		temp5 = otherHunter[0] % temp3
	else:
		temp5 = temp3
	if temp2 != 0:
		temp3 = otherHunter[1] / temp2
	else:
		temp3 = temp2
	return [ prey[1] , otherHunter[0] ]
