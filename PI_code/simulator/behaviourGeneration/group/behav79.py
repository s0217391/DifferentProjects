#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] + otherHunter[1]
	temp1 = prey[1] + otherHunter[1]
	temp2 = min( temp0 , prey[1] )
	temp1 = -1 * temp1
	if otherHunter[0] != 0:
		temp0 = prey[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp0 = temp2 * temp1
	temp0 = max( temp2 , temp2 )
	if otherHunter[1] > otherHunter[1] :
		temp0 = prey[0] + temp0
	else:
		if dist > temp0 :
			temp0 = max( prey[0] , temp2 )
		else:
			temp0 = prey[0] + temp0
	if temp2 != 0:
		temp0 = prey[1] % temp2
	else:
		temp0 = temp2
	temp0 = min( otherHunter[1] , dist )
	temp1 = temp2 - otherHunter[0]
	if prey[0] > temp0 :
		temp2 = -1 * prey[0]
	else:
		if prey[0] > temp1 :
			temp2 = max( temp1 , otherHunter[0] )
		else:
			temp2 = min( temp2 , otherHunter[1] )
	temp1 = max( temp0 , temp0 )
	if prey[1] != 0:
		temp3 = temp0 / prey[1]
	else:
		temp3 = prey[1]
	if otherHunter[1] > temp0 :
		if temp1 != 0:
			temp3 = otherHunter[1] / temp1
		else:
			temp3 = temp1
	else:
		if temp0 != 0:
			temp3 = prey[0] / temp0
		else:
			temp3 = temp0
	if temp2 > prey[1] :
		temp4 = min( temp1 , dist )
	else:
		temp4 = prey[1] * otherHunter[1]
	temp5 = temp1 + temp4
	if temp1 != 0:
		temp1 = temp4 / temp1
	else:
		temp1 = temp1
	if prey[0] > temp1 :
		temp4 = min( temp3 , temp0 )
	else:
		temp4 = max( temp3 , otherHunter[0] )
	temp2 = otherHunter[0] - otherHunter[1]
	temp1 = min( temp4 , dist )
	return [ prey[0] , temp1 ]
