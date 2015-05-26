#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[1] , prey[0] )
	temp1 = otherHunter[1] + prey[0]
	if dist > prey[1] :
		temp1 = prey[1] - otherHunter[0]
	else:
		temp1 = min( dist , dist )
	temp2 = dist - prey[0]
	return [ otherHunter[1] , otherHunter[0] ]
