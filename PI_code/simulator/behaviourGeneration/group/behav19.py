#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = otherHunter[0] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = max( prey[1] , dist )
	if temp1 != 0:
		temp0 = prey[1] % temp1
	else:
		temp0 = temp1
	if prey[1] != 0:
		temp0 = temp1 % prey[1]
	else:
		temp0 = prey[1]
	temp2 = prey[1] - prey[0]
	temp2 = max( dist , dist )
	temp1 = temp0 - temp2
	return [ prey[1] , temp0 ]