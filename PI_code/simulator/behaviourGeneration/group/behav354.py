#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[0] , prey[0] )
	if dist != 0:
		temp1 = temp0 / dist
	else:
		temp1 = dist
	temp0 = otherHunter[0] * otherHunter[0]
	if otherHunter[1] > dist :
		temp2 = max( prey[1] , temp1 )
	else:
		temp2 = max( otherHunter[1] , temp0 )
	if otherHunter[1] > temp0 :
		temp3 = max( prey[0] , temp1 )
	else:
		if dist != 0:
			temp3 = temp0 / dist
		else:
			temp3 = dist
	return [ temp1 , temp3 ]
