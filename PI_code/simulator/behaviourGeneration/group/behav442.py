#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] > dist :
		temp0 = max( prey[1] , otherHunter[0] )
	else:
		temp0 = prey[1] + otherHunter[1]
	temp1 = prey[0] - otherHunter[1]
	if otherHunter[1] != 0:
		temp2 = temp1 % otherHunter[1]
	else:
		temp2 = otherHunter[1]
	temp2 = dist + temp2
	temp2 = -1 * otherHunter[0]
	temp1 = dist + otherHunter[0]
	temp3 = prey[0] - dist
	return [ temp3 , prey[0] ]
