#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist - otherHunter[1]
	temp1 = prey[1] + prey[1]
	temp2 = -1 * otherHunter[0]
	temp0 = prey[0] * dist
	if prey[0] > otherHunter[1] :
		temp0 = min( temp0 , otherHunter[1] )
	else:
		temp0 = max( temp0 , prey[0] )
	temp1 = otherHunter[1] * dist
	temp2 = max( temp0 , temp2 )
	temp1 = max( otherHunter[0] , dist )
	temp2 = prey[1] * dist
	temp3 = -1 * temp0
	temp1 = temp1 + otherHunter[0]
	temp3 = -1 * dist
	if otherHunter[1] > temp2 :
		temp0 = temp1 - dist
	else:
		temp0 = min( temp1 , otherHunter[1] )
	temp0 = prey[0] - temp1
	return [ otherHunter[0] , temp1 ]
