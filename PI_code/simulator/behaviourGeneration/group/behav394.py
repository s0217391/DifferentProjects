#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] - otherHunter[1]
	temp1 = otherHunter[0] * prey[0]
	temp1 = prey[0] - otherHunter[1]
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	if otherHunter[1] != 0:
		temp1 = temp0 % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if otherHunter[1] > temp0 :
		temp0 = min( dist , dist )
	else:
		if otherHunter[1] != 0:
			temp0 = temp1 % otherHunter[1]
		else:
			temp0 = otherHunter[1]
	if otherHunter[1] > prey[0] :
		temp0 = max( prey[0] , temp1 )
	else:
		temp0 = otherHunter[0] * temp1
	temp0 = otherHunter[1] - dist
	temp2 = dist - prey[1]
	if prey[0] > temp0 :
		if dist != 0:
			temp2 = prey[0] / dist
		else:
			temp2 = dist
	else:
		if temp0 != 0:
			temp2 = prey[1] / temp0
		else:
			temp2 = temp0
	if temp2 != 0:
		temp1 = temp1 / temp2
	else:
		temp1 = temp2
	return [ temp1 , otherHunter[1] ]
