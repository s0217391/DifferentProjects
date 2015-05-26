#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = -1 * prey[1]
	temp1 = otherHunter[1] * temp0
	temp1 = -1 * prey[0]
	temp1 = dist + temp0
	temp1 = prey[1] + prey[0]
	temp2 = -1 * prey[0]
	temp0 = temp1 - otherHunter[0]
	temp2 = temp2 + prey[1]
	temp2 = max( otherHunter[0] , temp2 )
	temp3 = min( prey[0] , prey[0] )
	temp4 = max( temp0 , otherHunter[0] )
	temp4 = max( temp1 , temp0 )
	temp4 = -1 * prey[0]
	temp1 = max( dist , otherHunter[0] )
	return [ temp2 , temp0 ]
