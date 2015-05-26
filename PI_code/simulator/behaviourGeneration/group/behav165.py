#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] * otherHunter[0]
	temp1 = min( temp0 , temp0 )
	temp0 = temp0 + temp1
	temp0 = prey[0] + temp0
	temp1 = -1 * temp0
	return [ otherHunter[1] , temp1 ]
