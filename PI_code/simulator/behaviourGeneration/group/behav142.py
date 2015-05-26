#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] + prey[0]
	temp1 = otherHunter[0] * dist
	temp0 = min( temp0 , temp0 )
	temp1 = prey[1] * prey[1]
	temp0 = dist - temp0
	temp1 = max( otherHunter[1] , prey[1] )
	if otherHunter[1] != 0:
		temp0 = otherHunter[0] / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if prey[1] != 0:
		temp1 = prey[0] % prey[1]
	else:
		temp1 = prey[1]
	temp0 = otherHunter[0] + dist
	if prey[0] != 0:
		temp0 = otherHunter[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = max( otherHunter[1] , dist )
	if temp0 != 0:
		temp2 = temp0 / temp0
	else:
		temp2 = temp0
	temp2 = min( temp2 , otherHunter[0] )
	temp2 = temp0 * dist
	return [ prey[0] , temp1 ]
