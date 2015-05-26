#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist * otherHunter[1]
	if otherHunter[0] != 0:
		temp1 = otherHunter[1] / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp2 = -1 * temp1
	temp2 = temp0 * temp2
	if otherHunter[0] != 0:
		temp3 = prey[1] / otherHunter[0]
	else:
		temp3 = otherHunter[0]
	temp4 = min( dist , temp0 )
	temp2 = -1 * temp3
	temp5 = min( prey[1] , dist )
	if temp1 > prey[0] :
		temp6 = min( dist , temp1 )
	else:
		temp6 = -1 * temp1
	temp7 = -1 * temp1
	temp8 = otherHunter[1] + temp3
	temp8 = -1 * temp0
	temp1 = dist - otherHunter[1]
	temp6 = min( temp6 , prey[1] )
	temp2 = temp4 - temp7
	return [ temp7 , temp7 ]
