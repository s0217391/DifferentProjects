#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	if otherHunter[0] > dist :
		temp1 = min( otherHunter[0] , otherHunter[0] )
	else:
		if dist != 0:
			temp1 = dist / dist
		else:
			temp1 = dist
	temp2 = otherHunter[1] - temp0
	if otherHunter[1] != 0:
		temp1 = dist % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	return [ temp2 , otherHunter[0] ]
