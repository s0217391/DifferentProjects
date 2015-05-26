#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = otherHunter[0] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if dist != 0:
		temp1 = prey[0] / dist
	else:
		temp1 = dist
	temp0 = temp1 + otherHunter[0]
	temp1 = dist + otherHunter[1]
	temp0 = temp1 + otherHunter[0]
	if temp1 > prey[1] :
		if dist != 0:
			temp0 = dist / dist
		else:
			temp0 = dist
	else:
		temp0 = -1 * temp1
	temp2 = max( prey[0] , otherHunter[0] )
	temp1 = temp0 + otherHunter[1]
	if temp1 != 0:
		temp1 = dist % temp1
	else:
		temp1 = temp1
	if otherHunter[1] != 0:
		temp0 = otherHunter[1] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp2 = min( prey[0] , dist )
	temp0 = -1 * temp0
	if temp2 != 0:
		temp0 = temp0 / temp2
	else:
		temp0 = temp2
	temp1 = max( temp1 , prey[0] )
	temp2 = temp0 - temp1
	temp2 = otherHunter[1] + otherHunter[1]
	temp1 = -1 * temp0
	return [ temp1 , dist ]
