#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[0] , dist )
	if temp0 != 0:
		temp1 = otherHunter[0] / temp0
	else:
		temp1 = temp0
	if otherHunter[0] > temp0 :
		temp0 = max( otherHunter[1] , temp1 )
	else:
		temp0 = min( dist , temp1 )
	temp0 = prey[1] * otherHunter[0]
	return [ temp1 , temp0 ]
