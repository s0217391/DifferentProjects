#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[1] , prey[1] )
	temp1 = temp0 - otherHunter[0]
	if temp1 != 0:
		temp2 = prey[0] % temp1
	else:
		temp2 = temp1
	if temp0 > prey[1] :
		temp0 = temp2 - otherHunter[1]
	else:
		temp0 = min( temp0 , dist )
	if temp1 != 0:
		temp3 = dist % temp1
	else:
		temp3 = temp1
	if otherHunter[0] != 0:
		temp0 = temp0 % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp2 = temp2 + prey[1]
	return [ temp1 , prey[1] ]
