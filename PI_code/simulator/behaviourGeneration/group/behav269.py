#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , otherHunter[1] )
	if prey[1] > dist :
		temp1 = prey[1] * prey[1]
	else:
		if otherHunter[1] > otherHunter[0] :
			temp1 = -1 * otherHunter[0]
		else:
			temp1 = min( prey[1] , prey[0] )
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	temp2 = otherHunter[0] - dist
	temp2 = max( otherHunter[1] , dist )
	temp0 = prey[1] - temp1
	temp0 = max( otherHunter[1] , temp1 )
	temp3 = min( dist , otherHunter[0] )
	temp1 = min( temp2 , temp1 )
	temp3 = min( temp3 , prey[1] )
	temp3 = -1 * temp2
	if prey[0] != 0:
		temp4 = dist % prey[0]
	else:
		temp4 = prey[0]
	if prey[1] != 0:
		temp1 = otherHunter[0] % prey[1]
	else:
		temp1 = prey[1]
	temp0 = -1 * otherHunter[1]
	temp2 = max( prey[0] , dist )
	if temp2 != 0:
		temp0 = prey[0] / temp2
	else:
		temp0 = temp2
	temp1 = prey[0] * temp4
	temp1 = prey[0] * dist
	temp4 = min( temp1 , prey[0] )
	temp3 = max( temp0 , temp4 )
	return [ otherHunter[1] , otherHunter[0] ]
