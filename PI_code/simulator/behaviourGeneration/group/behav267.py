#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[0] , prey[1] )
	if temp0 != 0:
		temp1 = dist / temp0
	else:
		temp1 = temp0
	temp1 = prey[0] + otherHunter[0]
	if dist != 0:
		temp2 = otherHunter[1] / dist
	else:
		temp2 = dist
	temp2 = max( temp0 , prey[0] )
	if prey[1] != 0:
		temp3 = temp2 / prey[1]
	else:
		temp3 = prey[1]
	temp2 = temp2 * otherHunter[1]
	temp4 = otherHunter[0] - temp2
	temp0 = temp1 + temp3
	temp1 = -1 * temp2
	if dist != 0:
		temp0 = temp2 / dist
	else:
		temp0 = dist
	temp3 = temp4 - temp4
	if otherHunter[0] > temp4 :
		temp0 = -1 * temp0
	else:
		temp0 = dist - temp4
	temp2 = max( prey[1] , dist )
	if dist != 0:
		temp4 = otherHunter[1] % dist
	else:
		temp4 = dist
	temp1 = min( temp0 , otherHunter[1] )
	temp3 = -1 * otherHunter[1]
	temp5 = temp1 * dist
	if otherHunter[1] != 0:
		temp0 = dist % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp0 = max( temp1 , temp3 )
	temp0 = max( otherHunter[1] , temp1 )
	temp5 = -1 * prey[1]
	if temp2 != 0:
		temp4 = temp1 % temp2
	else:
		temp4 = temp2
	temp5 = min( dist , temp5 )
	if dist != 0:
		temp1 = dist % dist
	else:
		temp1 = dist
	return [ temp2 , temp1 ]
