#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[1] + otherHunter[0]
	temp1 = max( dist , prey[1] )
	if dist != 0:
		temp0 = temp0 % dist
	else:
		temp0 = dist
	if temp0 > dist :
		temp1 = prey[0] + temp1
	else:
		temp1 = min( prey[0] , temp1 )
	if temp0 > temp0 :
		temp2 = max( otherHunter[0] , prey[1] )
	else:
		temp2 = min( otherHunter[0] , otherHunter[1] )
	temp1 = -1 * prey[0]
	if temp2 != 0:
		temp1 = temp2 % temp2
	else:
		temp1 = temp2
	return [ prey[1] , otherHunter[1] ]
