#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[0] , dist )
	temp1 = prey[1] + dist
	temp1 = min( dist , prey[1] )
	temp0 = min( temp1 , dist )
	if temp1 != 0:
		temp1 = temp1 % temp1
	else:
		temp1 = temp1
	temp2 = dist - prey[1]
	if prey[0] > prey[0] :
		if otherHunter[0] != 0:
			temp0 = dist % otherHunter[0]
		else:
			temp0 = otherHunter[0]
	else:
		if temp2 != 0:
			temp0 = temp1 / temp2
		else:
			temp0 = temp2
	return [ otherHunter[1] , prey[0] ]
