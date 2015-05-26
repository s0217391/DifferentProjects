#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , otherHunter[0] )
	temp1 = -1 * temp0
	temp2 = max( dist , temp1 )
	temp1 = -1 * prey[0]
	temp1 = max( prey[1] , otherHunter[0] )
	temp3 = -1 * prey[1]
	temp3 = min( dist , temp3 )
	if temp0 > temp3 :
		temp4 = max( otherHunter[1] , prey[1] )
	else:
		temp4 = -1 * temp3
	return [ prey[1] , dist ]
