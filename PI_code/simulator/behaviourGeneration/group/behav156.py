#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , otherHunter[0] )
	temp1 = max( otherHunter[1] , prey[1] )
	temp2 = prey[1] + otherHunter[1]
	if temp2 != 0:
		temp2 = otherHunter[0] % temp2
	else:
		temp2 = temp2
	temp2 = otherHunter[1] - temp0
	if otherHunter[0] != 0:
		temp3 = otherHunter[1] / otherHunter[0]
	else:
		temp3 = otherHunter[0]
	if prey[0] != 0:
		temp0 = dist / prey[0]
	else:
		temp0 = prey[0]
	temp4 = temp2 * dist
	if dist != 0:
		temp2 = otherHunter[1] / dist
	else:
		temp2 = dist
	if temp0 != 0:
		temp3 = otherHunter[0] / temp0
	else:
		temp3 = temp0
	temp0 = otherHunter[1] - otherHunter[1]
	temp0 = max( otherHunter[1] , dist )
	temp2 = otherHunter[1] + prey[0]
	temp4 = max( temp0 , temp2 )
	if temp0 != 0:
		temp3 = prey[0] / temp0
	else:
		temp3 = temp0
	temp3 = min( temp3 , otherHunter[1] )
	return [ temp4 , temp4 ]
