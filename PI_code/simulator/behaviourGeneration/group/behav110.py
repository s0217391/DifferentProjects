#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[0] , dist )
	if dist != 0:
		temp1 = prey[1] / dist
	else:
		temp1 = dist
	temp2 = otherHunter[1] - temp1
	temp0 = prey[1] - temp0
	temp2 = -1 * temp0
	temp1 = min( prey[0] , otherHunter[1] )
	temp1 = max( temp2 , temp1 )
	if temp0 != 0:
		temp2 = otherHunter[1] / temp0
	else:
		temp2 = temp0
	if temp1 != 0:
		temp2 = otherHunter[1] % temp1
	else:
		temp2 = temp1
	return [ temp1 , otherHunter[1] ]
