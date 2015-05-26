#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = dist + otherHunter[1]
	if otherHunter[0] > otherHunter[1] :
		if otherHunter[1] > otherHunter[0] :
			temp1 = min( prey[0] , prey[1] )
		else:
			if dist != 0:
				temp1 = dist % dist
			else:
				temp1 = dist
	else:
		temp1 = temp0 + otherHunter[1]
	temp2 = min( prey[0] , prey[1] )
	temp0 = temp0 - temp1
	temp3 = max( prey[0] , otherHunter[1] )
	temp3 = -1 * dist
	temp3 = max( prey[1] , temp2 )
	temp1 = prey[0] * otherHunter[1]
	if prey[0] > temp1 :
		temp1 = temp2 - dist
	else:
		if otherHunter[1] > temp0 :
			temp1 = max( prey[1] , prey[0] )
		else:
			if prey[1] > dist :
				temp1 = min( temp3 , temp1 )
			else:
				temp1 = -1 * temp1
	if temp1 != 0:
		temp4 = dist % temp1
	else:
		temp4 = temp1
	temp3 = max( prey[1] , otherHunter[0] )
	temp4 = otherHunter[0] * temp2
	temp4 = temp3 + otherHunter[0]
	temp1 = -1 * dist
	if temp0 != 0:
		temp3 = temp0 / temp0
	else:
		temp3 = temp0
	if temp1 != 0:
		temp5 = temp4 % temp1
	else:
		temp5 = temp1
	if temp4 != 0:
		temp1 = temp1 % temp4
	else:
		temp1 = temp4
	temp6 = max( otherHunter[1] , temp5 )
	return [ otherHunter[0] , temp4 ]
