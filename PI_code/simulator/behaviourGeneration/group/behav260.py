#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , prey[1] )
	temp1 = temp0 + otherHunter[1]
	if prey[0] > dist :
		temp1 = max( prey[1] , dist )
	else:
		temp1 = prey[0] + temp1
	return [ prey[1] , temp1 ]
