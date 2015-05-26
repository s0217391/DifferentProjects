#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	temp1 = max( temp0 , otherHunter[0] )
	temp0 = min( temp1 , dist )
	if prey[1] != 0:
		temp1 = temp1 % prey[1]
	else:
		temp1 = prey[1]
	return [ temp1 , temp0 ]
