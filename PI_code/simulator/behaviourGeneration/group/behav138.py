#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , dist )
	temp1 = -1 * temp0
	temp2 = max( otherHunter[0] , prey[0] )
	temp0 = -1 * temp2
	return [ temp1 , temp2 ]
