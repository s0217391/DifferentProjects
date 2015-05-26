#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , prey[1] )
	temp1 = min( prey[0] , prey[1] )
	temp1 = -1 * dist
	if prey[1] != 0:
		temp1 = otherHunter[0] % prey[1]
	else:
		temp1 = prey[1]
	if dist != 0:
		temp2 = otherHunter[1] / dist
	else:
		temp2 = dist
	temp0 = min( dist , temp1 )
	if dist != 0:
		temp2 = prey[0] / dist
	else:
		temp2 = dist
	temp3 = min( prey[1] , prey[0] )
	temp1 = min( dist , temp0 )
	if temp3 > temp3 :
		temp1 = temp3 - temp3
	else:
		temp1 = -1 * prey[1]
	temp4 = -1 * temp1
	temp4 = temp4 * temp1
	temp3 = prey[0] + dist
	temp1 = max( prey[1] , prey[0] )
	if temp1 > otherHunter[0] :
		temp4 = min( temp2 , temp2 )
	else:
		if temp1 != 0:
			temp4 = prey[0] / temp1
		else:
			temp4 = temp1
	return [ otherHunter[0] , otherHunter[0] ]
