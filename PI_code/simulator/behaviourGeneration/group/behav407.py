#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , prey[0] )
	temp1 = temp0 - prey[1]
	temp1 = min( temp1 , temp1 )
	if otherHunter[1] > temp1 :
		temp0 = dist - otherHunter[0]
	else:
		if otherHunter[1] != 0:
			temp0 = dist % otherHunter[1]
		else:
			temp0 = otherHunter[1]
	if temp0 != 0:
		temp0 = temp1 % temp0
	else:
		temp0 = temp0
	temp1 = prey[1] * prey[1]
	temp1 = dist + temp0
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	temp1 = temp1 - dist
	if prey[0] > prey[0] :
		if temp1 != 0:
			temp1 = prey[0] % temp1
		else:
			temp1 = temp1
	else:
		temp1 = -1 * prey[0]
	temp0 = max( prey[0] , otherHunter[0] )
	if temp1 != 0:
		temp1 = temp0 % temp1
	else:
		temp1 = temp1
	return [ temp1 , dist ]
