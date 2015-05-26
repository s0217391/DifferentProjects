#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = dist / prey[0]
	else:
		temp0 = prey[0]
	temp1 = min( dist , prey[1] )
	temp2 = temp1 * dist
	temp0 = temp2 + temp2
	return [ temp0 , otherHunter[1] ]
