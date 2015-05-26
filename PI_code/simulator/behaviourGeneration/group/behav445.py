#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] + dist
	temp1 = min( prey[0] , prey[1] )
	if prey[0] != 0:
		temp1 = temp0 % prey[0]
	else:
		temp1 = prey[0]
	if otherHunter[0] > otherHunter[0] :
		temp0 = otherHunter[0] + otherHunter[0]
	else:
		temp0 = temp0 * dist
	if temp1 != 0:
		temp0 = otherHunter[0] / temp1
	else:
		temp0 = temp1
	temp0 = temp0 * prey[1]
	if otherHunter[0] != 0:
		temp0 = otherHunter[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if temp1 > prey[0] :
		if dist != 0:
			temp0 = otherHunter[0] % dist
		else:
			temp0 = dist
	else:
		if prey[1] != 0:
			temp0 = temp0 % prey[1]
		else:
			temp0 = prey[1]
	temp1 = temp1 - prey[0]
	temp0 = min( prey[1] , dist )
	return [ otherHunter[0] , prey[1] ]
