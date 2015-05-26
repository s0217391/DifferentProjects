#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[1] , prey[1] )
	temp1 = otherHunter[1] - prey[0]
	if temp1 != 0:
		temp0 = temp0 / temp1
	else:
		temp0 = temp1
	if temp1 != 0:
		temp1 = otherHunter[0] % temp1
	else:
		temp1 = temp1
	temp0 = prey[1] - temp1
	temp2 = prey[0] + temp1
	temp2 = temp2 - otherHunter[0]
	temp3 = max( temp0 , temp0 )
	temp3 = -1 * temp3
	if otherHunter[0] != 0:
		temp4 = otherHunter[1] / otherHunter[0]
	else:
		temp4 = otherHunter[0]
	temp0 = -1 * dist
	temp0 = min( temp4 , otherHunter[1] )
	if prey[1] != 0:
		temp5 = prey[0] % prey[1]
	else:
		temp5 = prey[1]
	if temp5 != 0:
		temp0 = prey[0] % temp5
	else:
		temp0 = temp5
	temp2 = temp0 * dist
	temp1 = prey[0] + temp2
	temp6 = max( otherHunter[1] , otherHunter[1] )
	if temp5 > temp6 :
		temp0 = temp4 + prey[1]
	else:
		temp0 = max( temp2 , temp6 )
	temp1 = min( temp4 , temp0 )
	temp3 = min( temp3 , dist )
	temp5 = min( dist , otherHunter[0] )
	temp0 = min( prey[0] , temp1 )
	if temp2 != 0:
		temp1 = temp3 / temp2
	else:
		temp1 = temp2
	return [ temp5 , prey[0] ]
