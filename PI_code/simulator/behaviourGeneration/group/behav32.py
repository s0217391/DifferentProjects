#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] - otherHunter[1]
	temp1 = otherHunter[1] * prey[0]
	temp0 = max( otherHunter[0] , prey[0] )
	return [ temp1 , prey[1] ]
