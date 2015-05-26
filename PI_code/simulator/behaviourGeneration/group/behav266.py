#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , otherHunter[1] )
	temp1 = -1 * otherHunter[1]
	temp2 = temp0 + otherHunter[0]
	temp2 = otherHunter[1] * dist
	temp2 = min( prey[0] , prey[1] )
	temp2 = min( temp2 , prey[0] )
	temp0 = max( otherHunter[0] , otherHunter[0] )
	if temp1 > temp0 :
		temp3 = max( prey[1] , dist )
	else:
		if temp0 != 0:
			temp3 = temp1 % temp0
		else:
			temp3 = temp0
	temp1 = min( temp0 , temp1 )
	if prey[0] != 0:
		temp0 = otherHunter[1] % prey[0]
	else:
		temp0 = prey[0]
	if temp3 > temp0 :
		temp0 = min( prey[0] , temp2 )
	else:
		temp0 = max( prey[0] , otherHunter[0] )
	if otherHunter[1] != 0:
		temp1 = otherHunter[0] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if otherHunter[1] > otherHunter[1] :
		temp0 = temp2 - temp0
	else:
		if prey[1] > temp3 :
			temp0 = min( dist , otherHunter[1] )
		else:
			temp0 = prey[0] * dist
	temp2 = -1 * prey[1]
	temp2 = dist + prey[0]
	temp3 = max( prey[1] , prey[1] )
	temp2 = min( dist , temp1 )
	temp3 = otherHunter[1] * prey[0]
	if temp1 != 0:
		temp4 = otherHunter[1] / temp1
	else:
		temp4 = temp1
	temp4 = -1 * temp2
	temp5 = temp1 * temp0
	return [ otherHunter[1] , temp0 ]
