#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , dist )
	temp1 = min( prey[1] , dist )
	temp2 = -1 * temp1
	if temp2 != 0:
		temp0 = temp1 / temp2
	else:
		temp0 = temp2
	temp1 = -1 * prey[0]
	if dist != 0:
		temp1 = temp1 / dist
	else:
		temp1 = dist
	temp0 = min( prey[1] , otherHunter[0] )
	temp2 = max( temp0 , temp2 )
	temp2 = max( temp2 , prey[0] )
	temp0 = otherHunter[1] + prey[0]
	return [ prey[1] , dist ]
