#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = otherHunter[0] / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = otherHunter[0] * otherHunter[1]
	temp2 = max( dist , dist )
	temp2 = min( otherHunter[0] , temp2 )
	temp0 = temp0 * temp2
	if prey[1] != 0:
		temp1 = temp1 / prey[1]
	else:
		temp1 = prey[1]
	temp1 = min( prey[1] , dist )
	temp0 = max( otherHunter[0] , prey[0] )
	temp0 = prey[0] * prey[0]
	temp1 = otherHunter[0] * dist
	if temp0 != 0:
		temp1 = otherHunter[1] / temp0
	else:
		temp1 = temp0
	temp3 = max( temp0 , temp1 )
	temp2 = otherHunter[0] - temp3
	temp1 = -1 * temp1
	temp4 = min( temp2 , prey[1] )
	if prey[1] != 0:
		temp4 = otherHunter[0] / prey[1]
	else:
		temp4 = prey[1]
	if prey[1] > prey[1] :
		temp0 = max( temp0 , temp4 )
	else:
		temp0 = max( dist , dist )
	temp4 = prey[0] * dist
	if temp0 != 0:
		temp5 = otherHunter[0] / temp0
	else:
		temp5 = temp0
	temp4 = min( temp1 , otherHunter[1] )
	temp0 = max( dist , temp1 )
	temp4 = prey[1] - temp0
	return [ temp2 , otherHunter[0] ]
