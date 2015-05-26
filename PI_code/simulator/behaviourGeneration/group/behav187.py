#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[0] , otherHunter[1] )
	temp1 = -1 * otherHunter[0]
	temp0 = min( otherHunter[1] , temp0 )
	temp1 = max( prey[0] , temp0 )
	temp2 = max( prey[1] , temp0 )
	temp3 = max( temp2 , prey[0] )
	temp4 = min( temp2 , temp3 )
	temp1 = -1 * temp3
	temp5 = max( temp0 , prey[1] )
	temp0 = -1 * otherHunter[1]
	return [ prey[1] , otherHunter[1] ]
