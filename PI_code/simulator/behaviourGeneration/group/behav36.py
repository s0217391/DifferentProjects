#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = dist % dist
	else:
		temp0 = dist
	if dist != 0:
		temp1 = prey[1] / dist
	else:
		temp1 = dist
	if temp0 != 0:
		temp1 = temp1 % temp0
	else:
		temp1 = temp0
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp0 = temp0 * prey[1]
	temp0 = temp0 - temp1
	temp2 = max( otherHunter[0] , dist )
	temp3 = max( temp2 , temp0 )
	temp2 = temp1 + temp2
	if temp2 != 0:
		temp1 = prey[0] / temp2
	else:
		temp1 = temp2
	temp3 = temp3 + prey[1]
	temp3 = temp1 + temp2
	temp1 = min( prey[0] , dist )
	temp3 = max( temp0 , temp3 )
	if temp0 != 0:
		temp0 = dist % temp0
	else:
		temp0 = temp0
	return [ temp2 , temp2 ]
