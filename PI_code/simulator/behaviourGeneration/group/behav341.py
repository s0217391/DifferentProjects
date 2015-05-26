#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + otherHunter[1]
	temp1 = prey[0] * temp0
	if otherHunter[1] > prey[0] :
		temp2 = max( prey[1] , otherHunter[0] )
	else:
		temp2 = otherHunter[1] - dist
	temp0 = prey[1] + temp0
	temp0 = max( otherHunter[1] , temp2 )
	temp3 = min( prey[1] , temp2 )
	temp4 = -1 * otherHunter[1]
	if temp2 > temp2 :
		temp5 = min( prey[1] , dist )
	else:
		temp5 = min( temp4 , temp4 )
	temp1 = prey[0] * temp3
	temp6 = min( temp0 , otherHunter[0] )
	temp2 = prey[1] * temp6
	if prey[1] != 0:
		temp1 = temp2 / prey[1]
	else:
		temp1 = prey[1]
	return [ temp6 , temp1 ]
