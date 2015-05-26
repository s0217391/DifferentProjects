#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] * prey[1]
	if temp0 != 0:
		temp1 = otherHunter[0] % temp0
	else:
		temp1 = temp0
	if prey[1] != 0:
		temp0 = otherHunter[1] / prey[1]
	else:
		temp0 = prey[1]
	temp0 = temp0 * temp0
	temp0 = dist * prey[0]
	temp1 = temp0 - prey[0]
	temp1 = min( otherHunter[1] , dist )
	if prey[1] != 0:
		temp1 = dist % prey[1]
	else:
		temp1 = prey[1]
	if otherHunter[0] > prey[0] :
		temp1 = min( prey[0] , temp1 )
	else:
		temp1 = prey[1] * temp0
	temp2 = otherHunter[0] - otherHunter[0]
	if temp1 != 0:
		temp2 = otherHunter[0] / temp1
	else:
		temp2 = temp1
	temp1 = -1 * otherHunter[0]
	temp3 = otherHunter[0] + temp2
	if prey[1] != 0:
		temp0 = otherHunter[0] / prey[1]
	else:
		temp0 = prey[1]
	temp3 = dist * dist
	if otherHunter[1] != 0:
		temp3 = temp3 / otherHunter[1]
	else:
		temp3 = otherHunter[1]
	temp4 = min( dist , temp1 )
	temp3 = otherHunter[1] + temp0
	temp0 = min( temp0 , otherHunter[0] )
	temp1 = otherHunter[0] + otherHunter[0]
	return [ temp3 , temp4 ]
