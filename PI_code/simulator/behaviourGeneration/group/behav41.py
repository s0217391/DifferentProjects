#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > otherHunter[1] :
		temp0 = prey[0] - dist
	else:
		temp0 = -1 * otherHunter[1]
	if temp0 != 0:
		temp1 = otherHunter[1] / temp0
	else:
		temp1 = temp0
	temp0 = -1 * otherHunter[1]
	if temp1 > otherHunter[0] :
		if prey[1] != 0:
			temp2 = otherHunter[0] % prey[1]
		else:
			temp2 = prey[1]
	else:
		if temp1 > prey[1] :
			temp2 = min( dist , dist )
		else:
			temp2 = otherHunter[1] + prey[0]
	temp0 = -1 * otherHunter[0]
	temp3 = prey[0] * dist
	temp0 = prey[0] - temp2
	temp3 = temp3 - dist
	if prey[1] > temp1 :
		temp2 = prey[1] - temp1
	else:
		if otherHunter[1] > dist :
			temp2 = temp3 * temp2
		else:
			temp2 = temp2 + temp2
	temp1 = min( otherHunter[1] , prey[0] )
	if dist != 0:
		temp4 = temp3 / dist
	else:
		temp4 = dist
	temp0 = -1 * prey[0]
	if temp0 != 0:
		temp2 = temp0 % temp0
	else:
		temp2 = temp0
	return [ prey[0] , prey[1] ]
