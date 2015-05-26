#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[1] , dist )
	temp1 = min( otherHunter[0] , dist )
	if otherHunter[1] != 0:
		temp2 = prey[0] % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	if otherHunter[1] != 0:
		temp0 = temp1 % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = prey[1] + temp0
	if otherHunter[1] != 0:
		temp1 = temp1 / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp3 = dist * otherHunter[1]
	if temp2 != 0:
		temp1 = temp2 % temp2
	else:
		temp1 = temp2
	return [ otherHunter[0] , prey[0] ]
