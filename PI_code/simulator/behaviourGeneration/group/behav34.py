#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = dist / prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * otherHunter[1]
	temp1 = max( otherHunter[1] , temp1 )
	temp1 = dist * otherHunter[1]
	temp2 = min( temp1 , dist )
	temp0 = temp2 + otherHunter[0]
	temp2 = prey[0] - prey[1]
	temp2 = prey[0] * prey[1]
	if prey[0] != 0:
		temp3 = prey[0] % prey[0]
	else:
		temp3 = prey[0]
	temp1 = temp0 + prey[1]
	temp2 = max( dist , otherHunter[0] )
	temp0 = max( temp2 , temp2 )
	temp0 = max( otherHunter[0] , temp1 )
	temp0 = max( prey[0] , temp0 )
	temp3 = max( dist , temp2 )
	temp4 = max( otherHunter[1] , otherHunter[0] )
	return [ prey[1] , temp1 ]
