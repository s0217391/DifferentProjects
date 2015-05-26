#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist - otherHunter[0]
	temp1 = -1 * dist
	temp1 = min( temp0 , temp1 )
	temp2 = -1 * dist
	temp3 = max( prey[1] , temp0 )
	if otherHunter[0] > temp3 :
		if temp3 > dist :
			temp4 = -1 * prey[1]
		else:
			temp4 = temp3 * otherHunter[1]
	else:
		if otherHunter[0] > prey[1] :
			temp4 = -1 * prey[0]
		else:
			temp4 = -1 * temp1
	temp0 = temp3 + temp3
	temp5 = max( dist , temp0 )
	temp2 = temp0 * temp4
	return [ temp2 , temp1 ]
