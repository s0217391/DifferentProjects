#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist > otherHunter[1] :
		temp0 = dist - prey[0]
	else:
		temp0 = prey[1] * dist
	temp1 = prey[1] * prey[0]
	temp2 = max( temp1 , temp1 )
	if temp2 > temp2 :
		temp2 = -1 * prey[1]
	else:
		temp2 = temp0 * prey[0]
	temp2 = min( prey[1] , dist )
	if otherHunter[1] != 0:
		temp0 = temp2 % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp3 = min( prey[1] , dist )
	temp2 = otherHunter[0] * prey[1]
	temp4 = dist * dist
	temp4 = temp3 + dist
	if temp4 != 0:
		temp4 = otherHunter[1] % temp4
	else:
		temp4 = temp4
	temp0 = max( temp0 , temp1 )
	temp4 = -1 * otherHunter[0]
	temp3 = temp2 - prey[1]
	temp1 = min( temp2 , temp3 )
	temp0 = prey[1] + temp2
	temp5 = max( temp1 , temp4 )
	temp1 = -1 * temp3
	temp6 = dist - temp2
	temp1 = -1 * temp5
	if temp2 != 0:
		temp4 = temp0 % temp2
	else:
		temp4 = temp2
	return [ temp1 , prey[0] ]
