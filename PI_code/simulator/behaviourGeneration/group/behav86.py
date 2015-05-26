#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if dist != 0:
		temp0 = otherHunter[0] / dist
	else:
		temp0 = dist
	if otherHunter[1] != 0:
		temp1 = otherHunter[1] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	temp2 = otherHunter[1] * dist
	if dist != 0:
		temp0 = temp2 / dist
	else:
		temp0 = dist
	if otherHunter[1] != 0:
		temp2 = otherHunter[0] / otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp0 = min( temp1 , prey[1] )
	temp3 = max( temp2 , otherHunter[0] )
	return [ temp2 , temp0 ]
