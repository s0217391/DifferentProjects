#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[0]
	temp1 = min( prey[1] , otherHunter[1] )
	temp0 = dist - prey[0]
	temp2 = max( dist , dist )
	temp0 = prey[0] * prey[0]
	temp3 = temp0 - temp1
	temp2 = otherHunter[0] * temp3
	if temp1 > temp1 :
		temp3 = min( dist , dist )
	else:
		temp3 = prey[1] - otherHunter[1]
	temp0 = temp3 * prey[1]
	temp3 = min( temp3 , prey[0] )
	temp0 = otherHunter[1] + temp3
	temp0 = otherHunter[1] - dist
	temp2 = max( otherHunter[0] , prey[1] )
	temp1 = -1 * otherHunter[1]
	temp2 = prey[0] * otherHunter[1]
	temp3 = temp1 - temp0
	temp3 = temp3 - prey[0]
	if temp2 != 0:
		temp1 = dist % temp2
	else:
		temp1 = temp2
	return [ temp0 , prey[0] ]
