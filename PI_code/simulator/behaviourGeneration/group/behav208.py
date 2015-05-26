#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = otherHunter[1] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = min( temp0 , otherHunter[0] )
	temp0 = prey[1] * prey[1]
	temp0 = otherHunter[0] + temp0
	temp2 = -1 * dist
	temp0 = otherHunter[0] * otherHunter[1]
	if temp0 > temp2 :
		temp1 = dist * temp1
	else:
		temp1 = temp2 * otherHunter[1]
	temp0 = temp2 * otherHunter[0]
	temp2 = max( temp0 , dist )
	if prey[1] > prey[1] :
		temp3 = temp0 * otherHunter[1]
	else:
		temp3 = prey[0] + temp1
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	temp1 = temp3 * prey[1]
	temp1 = max( temp3 , temp1 )
	temp4 = max( prey[1] , prey[0] )
	return [ prey[1] , prey[1] ]
