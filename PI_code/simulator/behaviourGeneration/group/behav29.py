#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] - prey[0]
	temp1 = min( otherHunter[0] , prey[0] )
	temp0 = otherHunter[0] + prey[0]
	temp2 = dist - otherHunter[1]
	temp1 = temp1 * prey[1]
	return [ otherHunter[0] , temp2 ]
