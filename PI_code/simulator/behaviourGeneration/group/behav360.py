#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( dist , otherHunter[0] )
	temp1 = prey[0] + dist
	if temp1 > dist :
		if otherHunter[0] != 0:
			temp2 = temp0 % otherHunter[0]
		else:
			temp2 = otherHunter[0]
	else:
		if dist != 0:
			temp2 = otherHunter[1] % dist
		else:
			temp2 = dist
	if temp2 != 0:
		temp3 = temp0 % temp2
	else:
		temp3 = temp2
	temp3 = dist + temp1
	return [ temp0 , otherHunter[0] ]
