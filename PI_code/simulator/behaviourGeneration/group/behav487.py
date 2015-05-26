#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , prey[1] )
	temp1 = dist * prey[0]
	temp0 = dist - otherHunter[0]
	if prey[1] != 0:
		temp2 = prey[1] / prey[1]
	else:
		temp2 = prey[1]
	temp0 = -1 * prey[0]
	if otherHunter[0] > otherHunter[0] :
		temp3 = min( prey[1] , dist )
	else:
		temp3 = temp2 + otherHunter[0]
	return [ prey[0] , prey[1] ]
