#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[0] , prey[1] )
	temp1 = max( prey[1] , prey[1] )
	temp0 = max( dist , otherHunter[1] )
	if temp0 != 0:
		temp2 = prey[0] % temp0
	else:
		temp2 = temp0
	temp3 = otherHunter[0] + prey[1]
	temp4 = prey[1] * temp2
	if temp3 != 0:
		temp1 = temp4 % temp3
	else:
		temp1 = temp3
	temp3 = min( otherHunter[1] , prey[1] )
	temp4 = otherHunter[0] + temp3
	temp1 = min( temp0 , otherHunter[1] )
	temp0 = max( temp4 , dist )
	if temp3 != 0:
		temp5 = otherHunter[1] / temp3
	else:
		temp5 = temp3
	temp6 = otherHunter[1] + prey[1]
	temp5 = temp5 + prey[0]
	return [ temp6 , prey[0] ]
