#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] * otherHunter[0]
	temp1 = otherHunter[0] * prey[1]
	if otherHunter[0] > prey[0] :
		temp2 = max( temp0 , otherHunter[1] )
	else:
		temp2 = otherHunter[1] + temp1
	temp2 = otherHunter[0] - dist
	temp1 = -1 * otherHunter[1]
	return [ temp0 , temp1 ]
