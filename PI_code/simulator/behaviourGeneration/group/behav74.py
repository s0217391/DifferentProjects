#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , otherHunter[0] )
	temp1 = max( prey[0] , dist )
	temp0 = min( otherHunter[1] , temp0 )
	if temp1 != 0:
		temp2 = otherHunter[1] / temp1
	else:
		temp2 = temp1
	if prey[1] > temp1 :
		temp3 = prey[1] * prey[0]
	else:
		temp3 = prey[0] - prey[0]
	temp4 = dist - dist
	temp4 = temp3 * otherHunter[0]
	temp2 = otherHunter[1] + prey[0]
	temp2 = otherHunter[1] - temp3
	return [ otherHunter[0] , dist ]
