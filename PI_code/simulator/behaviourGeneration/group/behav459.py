#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , otherHunter[1] )
	temp1 = min( otherHunter[1] , otherHunter[0] )
	if prey[0] != 0:
		temp0 = otherHunter[0] % prey[0]
	else:
		temp0 = prey[0]
	temp2 = max( dist , prey[0] )
	return [ temp1 , dist ]
