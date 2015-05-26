#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	temp1 = dist + otherHunter[0]
	if prey[0] > temp0 :
		temp1 = min( otherHunter[1] , otherHunter[0] )
	else:
		temp1 = min( temp0 , otherHunter[0] )
	if otherHunter[0] != 0:
		temp0 = prey[1] / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	return [ prey[1] , prey[1] ]
