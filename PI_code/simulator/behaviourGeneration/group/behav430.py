#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] - prey[0]
	if temp0 > prey[1] :
		temp1 = max( prey[1] , dist )
	else:
		temp1 = prey[1] - otherHunter[0]
	if otherHunter[1] != 0:
		temp0 = temp1 / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if dist > prey[0] :
		temp1 = -1 * otherHunter[1]
	else:
		temp1 = -1 * prey[1]
	temp2 = -1 * otherHunter[0]
	temp3 = prey[0] * temp0
	if temp1 != 0:
		temp3 = dist % temp1
	else:
		temp3 = temp1
	if otherHunter[0] != 0:
		temp1 = otherHunter[0] % otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp4 = otherHunter[1] + otherHunter[0]
	if temp2 != 0:
		temp0 = temp4 % temp2
	else:
		temp0 = temp2
	temp4 = otherHunter[1] - temp4
	temp4 = max( dist , otherHunter[1] )
	temp2 = dist * temp4
	temp2 = min( prey[0] , temp3 )
	temp0 = -1 * temp1
	temp1 = -1 * temp2
	return [ dist , dist ]
