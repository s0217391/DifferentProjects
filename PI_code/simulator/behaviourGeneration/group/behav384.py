#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , dist )
	temp1 = temp0 * dist
	temp0 = -1 * prey[0]
	if dist != 0:
		temp0 = dist % dist
	else:
		temp0 = dist
	temp1 = prey[1] + otherHunter[1]
	temp2 = otherHunter[1] - prey[0]
	if dist != 0:
		temp0 = otherHunter[1] / dist
	else:
		temp0 = dist
	temp2 = temp0 - otherHunter[0]
	temp2 = temp2 + temp1
	if prey[0] != 0:
		temp2 = temp0 % prey[0]
	else:
		temp2 = prey[0]
	temp3 = prey[0] + otherHunter[0]
	if temp0 != 0:
		temp0 = temp1 / temp0
	else:
		temp0 = temp0
	temp0 = max( otherHunter[0] , otherHunter[1] )
	if temp2 > otherHunter[0] :
		if temp1 > prey[1] :
			temp1 = otherHunter[0] * otherHunter[1]
		else:
			temp1 = max( otherHunter[0] , temp0 )
	else:
		temp1 = min( temp0 , temp3 )
	return [ otherHunter[1] , otherHunter[1] ]
