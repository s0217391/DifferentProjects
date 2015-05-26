#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] - otherHunter[1]
	if dist != 0:
		temp1 = otherHunter[1] % dist
	else:
		temp1 = dist
	temp2 = -1 * temp0
	temp3 = -1 * temp2
	temp1 = otherHunter[1] - temp2
	temp4 = prey[1] + otherHunter[0]
	temp0 = temp3 + temp0
	if temp3 > temp4 :
		temp2 = min( temp0 , prey[0] )
	else:
		temp2 = max( prey[0] , otherHunter[1] )
	temp4 = -1 * temp0
	if temp2 > prey[0] :
		temp0 = temp4 + prey[0]
	else:
		temp0 = min( temp2 , temp4 )
	temp4 = min( otherHunter[1] , prey[0] )
	temp3 = max( temp1 , dist )
	if prey[0] > otherHunter[0] :
		temp3 = min( prey[1] , temp1 )
	else:
		temp3 = prey[0] + temp1
	temp5 = max( temp1 , otherHunter[1] )
	temp0 = -1 * otherHunter[1]
	if dist != 0:
		temp1 = temp2 / dist
	else:
		temp1 = dist
	if temp5 != 0:
		temp3 = prey[1] / temp5
	else:
		temp3 = temp5
	temp1 = temp0 + dist
	temp0 = -1 * prey[1]
	if temp3 != 0:
		temp1 = temp1 % temp3
	else:
		temp1 = temp3
	return [ temp0 , temp5 ]
