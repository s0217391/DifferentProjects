#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] + otherHunter[0]
	temp1 = min( otherHunter[0] , prey[1] )
	temp1 = dist - temp0
	temp1 = max( otherHunter[1] , prey[0] )
	temp1 = min( dist , prey[1] )
	if prey[0] > temp1 :
		temp2 = otherHunter[0] + prey[1]
	else:
		temp2 = temp1 - temp0
	if prey[0] != 0:
		temp2 = prey[1] % prey[0]
	else:
		temp2 = prey[0]
	temp1 = max( otherHunter[1] , temp0 )
	temp0 = max( dist , prey[1] )
	temp3 = temp0 * temp2
	temp1 = dist + temp3
	if temp2 != 0:
		temp3 = temp0 / temp2
	else:
		temp3 = temp2
	if temp2 > temp2 :
		if temp2 > prey[1] :
			temp1 = min( temp0 , prey[1] )
		else:
			temp1 = min( temp1 , dist )
	else:
		temp1 = min( prey[0] , temp0 )
	temp0 = temp0 - dist
	temp4 = min( otherHunter[0] , dist )
	temp4 = max( temp0 , temp0 )
	if temp1 != 0:
		temp1 = dist % temp1
	else:
		temp1 = temp1
	temp4 = -1 * temp4
	temp3 = otherHunter[0] + temp2
	return [ temp0 , dist ]
