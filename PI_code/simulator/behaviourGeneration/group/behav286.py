#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[0] , dist )
	temp1 = otherHunter[1] + prey[0]
	if temp0 > temp0 :
		temp0 = -1 * temp0
	else:
		temp0 = temp0 * otherHunter[1]
	if otherHunter[0] != 0:
		temp0 = dist % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = min( prey[1] , otherHunter[1] )
	temp0 = prey[1] * prey[1]
	temp0 = otherHunter[0] * dist
	temp1 = prey[1] - prey[1]
	temp0 = min( temp1 , dist )
	if prey[0] != 0:
		temp1 = dist % prey[0]
	else:
		temp1 = prey[0]
	temp0 = -1 * otherHunter[0]
	temp1 = dist * otherHunter[0]
	temp0 = prey[0] + prey[1]
	if dist != 0:
		temp1 = otherHunter[1] % dist
	else:
		temp1 = dist
	temp1 = otherHunter[0] - temp1
	temp1 = otherHunter[1] * temp0
	return [ prey[1] , prey[1] ]
