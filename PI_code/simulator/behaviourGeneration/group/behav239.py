#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist + prey[0]
	temp1 = prey[1] - otherHunter[1]
	temp0 = prey[1] + temp1
	temp2 = min( temp1 , dist )
	if temp1 > prey[0] :
		temp2 = min( otherHunter[0] , otherHunter[0] )
	else:
		if temp2 > temp2 :
			temp2 = temp0 - prey[1]
		else:
			temp2 = prey[0] + otherHunter[0]
	temp3 = min( temp1 , otherHunter[0] )
	temp3 = min( otherHunter[0] , otherHunter[0] )
	temp4 = min( prey[1] , temp3 )
	temp1 = -1 * temp4
	temp5 = otherHunter[0] - temp3
	temp0 = min( temp3 , dist )
	if temp0 != 0:
		temp5 = temp4 / temp0
	else:
		temp5 = temp0
	if otherHunter[0] > temp4 :
		if otherHunter[1] > otherHunter[1] :
			temp6 = temp4 - dist
		else:
			temp6 = temp0 - temp2
	else:
		temp6 = -1 * temp0
	temp0 = min( temp1 , temp5 )
	temp4 = -1 * dist
	if temp6 != 0:
		temp6 = prey[0] % temp6
	else:
		temp6 = temp6
	temp1 = min( temp5 , prey[1] )
	if temp1 != 0:
		temp6 = temp5 % temp1
	else:
		temp6 = temp1
	temp6 = min( prey[1] , temp1 )
	temp0 = temp2 * temp6
	if prey[0] != 0:
		temp6 = dist % prey[0]
	else:
		temp6 = prey[0]
	return [ temp1 , temp0 ]
