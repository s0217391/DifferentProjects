#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = dist / prey[0]
	else:
		temp0 = prey[0]
	temp1 = min( temp0 , dist )
	temp2 = min( temp1 , prey[0] )
	temp3 = min( temp2 , temp1 )
	if temp2 != 0:
		temp0 = temp0 / temp2
	else:
		temp0 = temp2
	temp2 = -1 * dist
	return [ otherHunter[1] , prey[0] ]
