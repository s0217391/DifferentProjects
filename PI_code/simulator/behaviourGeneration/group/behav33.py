#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] - dist
	temp1 = temp0 + temp0
	temp2 = min( temp0 , prey[0] )
	if temp2 > prey[0] :
		temp2 = prey[0] - prey[0]
	else:
		temp2 = otherHunter[0] + otherHunter[0]
	return [ prey[1] , temp0 ]
