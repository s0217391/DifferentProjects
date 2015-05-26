#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , dist )
	if prey[1] > dist :
		temp1 = temp0 * dist
	else:
		temp1 = otherHunter[1] - otherHunter[1]
	if dist != 0:
		temp0 = otherHunter[1] / dist
	else:
		temp0 = dist
	if dist != 0:
		temp1 = temp1 % dist
	else:
		temp1 = dist
	if temp0 != 0:
		temp1 = otherHunter[0] % temp0
	else:
		temp1 = temp0
	temp0 = max( temp0 , prey[1] )
	temp1 = max( prey[1] , otherHunter[1] )
	return [ otherHunter[0] , temp0 ]
