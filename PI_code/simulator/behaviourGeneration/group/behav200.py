#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[1] , otherHunter[1] )
	temp1 = min( otherHunter[1] , otherHunter[0] )
	if otherHunter[1] > otherHunter[1] :
		if otherHunter[0] != 0:
			temp1 = temp0 / otherHunter[0]
		else:
			temp1 = otherHunter[0]
	else:
		temp1 = min( otherHunter[0] , temp0 )
	if dist > temp0 :
		if temp1 != 0:
			temp0 = dist / temp1
		else:
			temp0 = temp1
	else:
		temp0 = temp0 + otherHunter[1]
	if temp0 != 0:
		temp0 = temp0 % temp0
	else:
		temp0 = temp0
	temp1 = temp1 + prey[0]
	if otherHunter[1] != 0:
		temp1 = otherHunter[1] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if otherHunter[1] > temp1 :
		temp1 = dist - prey[0]
	else:
		if otherHunter[0] != 0:
			temp1 = prey[1] / otherHunter[0]
		else:
			temp1 = otherHunter[0]
	temp0 = prey[1] - otherHunter[0]
	temp1 = min( prey[0] , dist )
	return [ prey[0] , temp0 ]
