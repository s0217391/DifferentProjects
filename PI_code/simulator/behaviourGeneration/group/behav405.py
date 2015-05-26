#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[0] , prey[1] )
	temp1 = min( temp0 , otherHunter[0] )
	temp1 = prey[0] - temp0
	temp1 = otherHunter[0] - prey[1]
	temp2 = max( prey[0] , temp1 )
	return [ dist , temp1 ]
