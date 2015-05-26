#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( otherHunter[0] , prey[0] )
	temp1 = prey[0] * prey[0]
	temp0 = max( prey[0] , temp0 )
	temp1 = min( otherHunter[1] , temp0 )
	if prey[0] > prey[0] :
		temp0 = prey[0] * prey[0]
	else:
		temp0 = min( temp0 , prey[0] )
	if temp0 > temp0 :
		temp2 = max( temp0 , otherHunter[0] )
	else:
		temp2 = otherHunter[0] - dist
	if otherHunter[1] > dist :
		temp1 = -1 * prey[0]
	else:
		temp1 = -1 * prey[0]
	temp3 = min( dist , prey[1] )
	temp1 = otherHunter[0] + temp1
	temp4 = min( prey[1] , temp3 )
	temp2 = max( temp3 , otherHunter[0] )
	temp2 = temp3 + otherHunter[0]
	return [ otherHunter[1] , temp1 ]
