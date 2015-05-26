#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[0] , otherHunter[1] )
	if otherHunter[1] != 0:
		temp1 = otherHunter[1] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if prey[0] != 0:
		temp2 = otherHunter[0] / prey[0]
	else:
		temp2 = prey[0]
	temp1 = otherHunter[1] + temp0
	if otherHunter[0] > temp1 :
		temp3 = otherHunter[0] - otherHunter[1]
	else:
		temp3 = max( otherHunter[1] , temp1 )
	temp2 = temp0 - temp1
	temp4 = max( prey[0] , prey[1] )
	temp0 = temp4 - temp4
	temp0 = prey[1] - otherHunter[0]
	temp4 = prey[1] * temp0
	return [ temp0 , prey[0] ]
