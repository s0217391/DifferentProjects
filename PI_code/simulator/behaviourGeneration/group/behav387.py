#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = prey[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = -1 * dist
	temp2 = otherHunter[0] * otherHunter[0]
	temp3 = prey[0] - temp2
	temp0 = dist - dist
	temp1 = -1 * otherHunter[0]
	temp4 = min( dist , otherHunter[1] )
	temp4 = max( temp2 , prey[0] )
	temp0 = max( otherHunter[0] , dist )
	temp1 = max( temp2 , temp1 )
	temp2 = temp4 * temp3
	temp0 = dist + temp4
	if temp2 != 0:
		temp2 = otherHunter[0] / temp2
	else:
		temp2 = temp2
	temp1 = otherHunter[1] - otherHunter[1]
	temp4 = max( temp1 , otherHunter[0] )
	temp3 = prey[1] - prey[1]
	temp1 = otherHunter[1] + dist
	return [ prey[1] , otherHunter[1] ]
