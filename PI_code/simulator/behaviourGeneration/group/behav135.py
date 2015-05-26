#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist - dist
	temp1 = otherHunter[0] + prey[0]
	temp0 = max( prey[0] , otherHunter[1] )
	if temp1 != 0:
		temp2 = dist % temp1
	else:
		temp2 = temp1
	if otherHunter[1] > temp2 :
		temp1 = -1 * temp0
	else:
		temp1 = temp1 - temp0
	temp3 = -1 * dist
	temp2 = prey[0] + otherHunter[0]
	temp3 = temp0 + temp0
	if temp2 != 0:
		temp1 = prey[1] % temp2
	else:
		temp1 = temp2
	if temp3 > temp2 :
		temp1 = prey[1] - prey[0]
	else:
		temp1 = -1 * dist
	if otherHunter[1] != 0:
		temp2 = temp3 / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp1 = temp1 + temp3
	temp0 = prey[0] + prey[0]
	temp3 = max( temp1 , temp1 )
	return [ dist , dist ]
