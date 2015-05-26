#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[0]
	temp1 = max( otherHunter[1] , otherHunter[1] )
	temp1 = otherHunter[0] - temp0
	if prey[0] > prey[1] :
		temp0 = max( dist , dist )
	else:
		temp0 = temp1 * otherHunter[1]
	temp0 = min( otherHunter[0] , temp1 )
	temp0 = prey[0] - prey[0]
	temp0 = temp0 + temp0
	if otherHunter[0] != 0:
		temp0 = otherHunter[1] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = otherHunter[0] - prey[0]
	temp1 = max( prey[1] , temp1 )
	temp1 = max( prey[0] , otherHunter[1] )
	if temp1 != 0:
		temp1 = dist % temp1
	else:
		temp1 = temp1
	temp2 = otherHunter[0] + prey[0]
	temp0 = otherHunter[0] - prey[1]
	if prey[0] > otherHunter[0] :
		temp0 = min( dist , temp2 )
	else:
		temp0 = prey[1] * temp2
	temp2 = -1 * prey[0]
	temp3 = -1 * temp0
	if prey[0] != 0:
		temp3 = temp2 % prey[0]
	else:
		temp3 = prey[0]
	temp0 = -1 * dist
	temp3 = temp1 - temp2
	temp1 = prey[0] - temp0
	if temp2 != 0:
		temp2 = otherHunter[1] % temp2
	else:
		temp2 = temp2
	temp1 = dist * temp0
	return [ temp1 , temp3 ]
