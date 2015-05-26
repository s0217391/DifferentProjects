#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] - otherHunter[0]
	temp1 = -1 * prey[0]
	temp0 = max( temp0 , otherHunter[0] )
	temp1 = temp0 * dist
	return [ otherHunter[0] , temp0 ]
