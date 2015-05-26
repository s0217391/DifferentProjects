#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] > otherHunter[1] :
		if prey[0] != 0:
			temp0 = otherHunter[1] / prey[0]
		else:
			temp0 = prey[0]
	else:
		temp0 = dist * prey[1]
	temp1 = min( prey[0] , temp0 )
	if temp1 != 0:
		temp0 = otherHunter[1] % temp1
	else:
		temp0 = temp1
	if prey[0] != 0:
		temp2 = otherHunter[1] / prey[0]
	else:
		temp2 = prey[0]
	temp3 = prey[0] - temp1
	temp1 = otherHunter[1] + otherHunter[1]
	if temp0 > dist :
		temp3 = min( temp2 , temp0 )
	else:
		temp3 = max( prey[1] , temp3 )
	temp1 = prey[0] * temp0
	temp3 = min( otherHunter[0] , temp1 )
	temp1 = temp0 + temp3
	temp3 = min( temp3 , otherHunter[1] )
	temp0 = temp2 * prey[0]
	if temp2 > temp3 :
		temp2 = otherHunter[1] + temp2
	else:
		temp2 = dist + temp0
	temp1 = otherHunter[1] - temp1
	temp2 = max( dist , temp1 )
	return [ otherHunter[0] , otherHunter[1] ]
