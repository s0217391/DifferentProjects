#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > otherHunter[1] :
		temp0 = max( otherHunter[1] , dist )
	else:
		temp0 = prey[0] + dist
	if prey[1] > otherHunter[0] :
		temp1 = otherHunter[1] + prey[1]
	else:
		if dist > otherHunter[1] :
			temp1 = -1 * otherHunter[1]
		else:
			temp1 = min( temp0 , otherHunter[0] )
	temp0 = max( prey[0] , prey[0] )
	temp2 = dist - dist
	temp0 = temp1 + dist
	temp0 = min( temp2 , otherHunter[1] )
	temp3 = prey[0] + temp1
	temp1 = min( dist , temp0 )
	if temp3 != 0:
		temp0 = temp1 % temp3
	else:
		temp0 = temp3
	if otherHunter[1] != 0:
		temp1 = temp1 % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if temp3 > temp1 :
		if otherHunter[0] != 0:
			temp1 = dist / otherHunter[0]
		else:
			temp1 = otherHunter[0]
	else:
		temp1 = temp2 * otherHunter[0]
	if temp3 != 0:
		temp0 = prey[1] % temp3
	else:
		temp0 = temp3
	if otherHunter[1] != 0:
		temp4 = prey[0] / otherHunter[1]
	else:
		temp4 = otherHunter[1]
	temp1 = otherHunter[1] * prey[1]
	temp3 = min( temp3 , temp3 )
	temp3 = prey[0] + temp4
	temp0 = dist + temp4
	temp3 = max( temp4 , prey[1] )
	temp2 = temp0 + temp1
	temp3 = max( dist , temp2 )
	temp4 = temp2 + prey[0]
	temp3 = temp1 * temp3
	if temp0 != 0:
		temp1 = otherHunter[1] / temp0
	else:
		temp1 = temp0
	return [ temp1 , otherHunter[0] ]
