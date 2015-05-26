#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * otherHunter[1]
	temp1 = otherHunter[0] + dist
	temp1 = otherHunter[0] + temp1
	temp1 = dist - temp1
	if prey[1] != 0:
		temp2 = temp0 % prey[1]
	else:
		temp2 = prey[1]
	temp1 = dist * prey[1]
	if otherHunter[1] > otherHunter[1] :
		temp1 = max( prey[1] , otherHunter[1] )
	else:
		temp1 = prey[0] - temp1
	if otherHunter[0] != 0:
		temp0 = prey[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp3 = max( temp0 , dist )
	temp4 = max( temp0 , otherHunter[0] )
	if prey[0] > temp1 :
		temp2 = max( temp4 , prey[0] )
	else:
		temp2 = otherHunter[0] * temp1
	if prey[0] != 0:
		temp1 = temp4 / prey[0]
	else:
		temp1 = prey[0]
	temp5 = temp1 * otherHunter[0]
	temp3 = max( prey[0] , temp3 )
	temp3 = -1 * temp0
	temp6 = max( otherHunter[0] , temp2 )
	if temp1 > temp5 :
		temp3 = temp4 + prey[0]
	else:
		temp3 = -1 * temp2
	return [ dist , temp6 ]
