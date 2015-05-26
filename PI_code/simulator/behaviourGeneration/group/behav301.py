#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , otherHunter[0] )
	if otherHunter[0] != 0:
		temp1 = prey[0] / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp0 = temp0 + otherHunter[1]
	temp2 = prey[1] * otherHunter[1]
	temp1 = otherHunter[1] + dist
	if prey[0] != 0:
		temp3 = temp2 % prey[0]
	else:
		temp3 = prey[0]
	temp3 = min( otherHunter[0] , temp3 )
	if otherHunter[1] > prey[1] :
		temp3 = max( otherHunter[0] , temp0 )
	else:
		temp3 = min( temp3 , temp3 )
	temp1 = min( prey[0] , prey[1] )
	temp2 = -1 * prey[1]
	if temp3 > temp0 :
		temp0 = min( dist , otherHunter[1] )
	else:
		temp0 = -1 * prey[1]
	temp0 = temp2 + prey[1]
	temp1 = min( dist , dist )
	temp2 = otherHunter[0] * prey[1]
	temp1 = prey[1] * temp1
	temp0 = prey[1] - temp2
	return [ temp2 , temp0 ]
