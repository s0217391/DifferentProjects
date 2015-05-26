#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] > prey[0] :
		temp0 = otherHunter[1] * prey[0]
	else:
		temp0 = -1 * prey[0]
	temp1 = prey[1] + temp0
	if prey[1] > temp0 :
		temp0 = max( temp1 , prey[0] )
	else:
		temp0 = dist * prey[1]
	return [ temp0 , temp0 ]
