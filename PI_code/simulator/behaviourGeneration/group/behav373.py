#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	temp1 = max( otherHunter[0] , dist )
	temp1 = -1 * otherHunter[0]
	temp0 = otherHunter[0] * prey[1]
	temp2 = prey[0] * temp0
	return [ dist , prey[1] ]
