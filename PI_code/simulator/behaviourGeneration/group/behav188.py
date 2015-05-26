#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , otherHunter[0] )
	temp1 = prey[0] * temp0
	temp1 = temp0 - prey[1]
	temp1 = max( temp1 , otherHunter[1] )
	if temp0 != 0:
		temp1 = dist / temp0
	else:
		temp1 = temp0
	temp2 = max( temp1 , dist )
	temp1 = dist + temp0
	temp0 = temp1 * temp1
	temp0 = -1 * dist
	if prey[0] != 0:
		temp3 = temp0 % prey[0]
	else:
		temp3 = prey[0]
	if otherHunter[0] > prey[1] :
		temp2 = prey[0] + prey[0]
	else:
		temp2 = otherHunter[1] + otherHunter[1]
	return [ otherHunter[0] , otherHunter[0] ]
