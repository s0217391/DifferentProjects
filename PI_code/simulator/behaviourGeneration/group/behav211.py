#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = prey[0] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = otherHunter[0] * prey[0]
	temp2 = prey[0] - prey[0]
	if otherHunter[0] != 0:
		temp3 = otherHunter[0] / otherHunter[0]
	else:
		temp3 = otherHunter[0]
	if otherHunter[0] > temp0 :
		temp3 = max( prey[0] , temp1 )
	else:
		temp3 = temp2 * temp1
	temp3 = max( temp3 , temp2 )
	temp3 = max( dist , otherHunter[0] )
	if prey[0] > temp0 :
		temp3 = temp1 - prey[1]
	else:
		temp3 = -1 * temp0
	temp2 = -1 * prey[0]
	if dist != 0:
		temp2 = temp1 / dist
	else:
		temp2 = dist
	temp0 = prey[1] + prey[1]
	return [ otherHunter[1] , temp2 ]
