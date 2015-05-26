#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = otherHunter[1] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = max( otherHunter[0] , prey[1] )
	temp1 = -1 * dist
	temp1 = min( temp0 , otherHunter[0] )
	temp2 = min( dist , dist )
	if otherHunter[1] != 0:
		temp0 = prey[0] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp1 = otherHunter[1] + temp1
	temp0 = min( prey[1] , dist )
	temp0 = max( otherHunter[1] , otherHunter[1] )
	if temp0 != 0:
		temp0 = temp2 % temp0
	else:
		temp0 = temp0
	temp1 = temp1 - temp2
	if otherHunter[1] > temp0 :
		if dist > prey[1] :
			temp3 = otherHunter[1] - dist
		else:
			temp3 = prey[1] * prey[0]
	else:
		temp3 = -1 * dist
	if otherHunter[1] != 0:
		temp0 = dist / otherHunter[1]
	else:
		temp0 = otherHunter[1]
	temp0 = temp0 * dist
	return [ temp1 , prey[0] ]
