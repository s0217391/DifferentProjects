#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * dist
	temp1 = temp0 * temp0
	temp1 = prey[1] - prey[0]
	if dist != 0:
		temp1 = temp1 % dist
	else:
		temp1 = dist
	if otherHunter[0] != 0:
		temp1 = otherHunter[1] / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp0 = otherHunter[1] - otherHunter[1]
	temp2 = max( otherHunter[0] , dist )
	return [ temp1 , prey[1] ]
