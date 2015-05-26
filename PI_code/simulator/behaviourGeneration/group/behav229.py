#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = dist % prey[1]
	else:
		temp0 = prey[1]
	if temp0 != 0:
		temp1 = dist % temp0
	else:
		temp1 = temp0
	temp2 = -1 * prey[0]
	temp1 = -1 * temp2
	temp3 = min( otherHunter[1] , dist )
	temp3 = -1 * dist
	if temp1 > otherHunter[0] :
		temp2 = min( otherHunter[1] , prey[0] )
	else:
		temp2 = temp2 + dist
	temp4 = min( dist , otherHunter[1] )
	temp4 = temp0 + prey[1]
	temp4 = temp2 * temp1
	temp5 = temp3 + temp2
	if otherHunter[1] > temp3 :
		temp5 = max( temp3 , temp0 )
	else:
		temp5 = prey[0] * temp2
	temp6 = -1 * prey[0]
	temp3 = min( temp4 , dist )
	temp3 = min( temp3 , otherHunter[0] )
	temp1 = -1 * prey[1]
	if temp2 != 0:
		temp3 = temp2 / temp2
	else:
		temp3 = temp2
	temp1 = min( temp6 , temp0 )
	temp4 = min( temp0 , prey[1] )
	temp5 = prey[0] + temp0
	temp2 = prey[0] + temp5
	if temp0 != 0:
		temp1 = temp3 / temp0
	else:
		temp1 = temp0
	temp7 = -1 * temp6
	temp3 = otherHunter[0] * dist
	return [ temp4 , prey[0] ]
