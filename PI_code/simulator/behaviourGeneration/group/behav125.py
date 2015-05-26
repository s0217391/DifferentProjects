#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , otherHunter[1] )
	temp1 = prey[0] + temp0
	temp1 = min( prey[0] , prey[0] )
	if otherHunter[0] > prey[0] :
		temp0 = -1 * dist
	else:
		temp0 = -1 * otherHunter[1]
	if otherHunter[1] != 0:
		temp1 = otherHunter[1] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp2 = -1 * otherHunter[1]
	temp3 = max( temp0 , temp1 )
	temp4 = otherHunter[0] - prey[0]
	if dist != 0:
		temp3 = temp0 % dist
	else:
		temp3 = dist
	if dist != 0:
		temp3 = prey[0] % dist
	else:
		temp3 = dist
	temp1 = -1 * prey[1]
	if otherHunter[1] != 0:
		temp2 = prey[0] % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp5 = min( otherHunter[0] , temp3 )
	temp1 = -1 * prey[0]
	temp0 = otherHunter[0] - temp1
	if temp0 > prey[0] :
		temp1 = temp0 + otherHunter[1]
	else:
		temp1 = min( otherHunter[0] , temp3 )
	temp6 = -1 * temp1
	temp5 = -1 * otherHunter[0]
	temp3 = -1 * temp1
	temp2 = temp4 * temp0
	temp7 = temp4 * prey[1]
	temp5 = max( temp7 , dist )
	temp6 = temp7 + otherHunter[1]
	temp2 = temp5 * prey[1]
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	return [ temp2 , temp5 ]
