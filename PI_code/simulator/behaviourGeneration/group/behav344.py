#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = otherHunter[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = min( prey[1] , dist )
	temp0 = temp0 + otherHunter[1]
	if dist != 0:
		temp2 = otherHunter[1] / dist
	else:
		temp2 = dist
	temp0 = max( otherHunter[0] , temp1 )
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	if temp1 != 0:
		temp0 = temp1 % temp1
	else:
		temp0 = temp1
	return [ temp1 , otherHunter[0] ]
