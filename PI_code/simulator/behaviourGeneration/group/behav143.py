#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = dist % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = temp0 * prey[1]
	temp1 = otherHunter[0] + prey[0]
	temp2 = max( temp0 , prey[0] )
	temp3 = temp1 + temp1
	if otherHunter[0] > prey[0] :
		temp4 = otherHunter[1] + prey[1]
	else:
		temp4 = temp0 + prey[1]
	temp1 = temp4 * temp1
	temp5 = dist * otherHunter[0]
	temp6 = min( temp3 , prey[0] )
	if temp4 > temp3 :
		temp6 = -1 * temp6
	else:
		if temp0 > temp3 :
			temp6 = prey[0] + temp4
		else:
			temp6 = max( temp6 , temp4 )
	if temp0 > prey[0] :
		temp2 = temp6 * otherHunter[0]
	else:
		temp2 = dist * temp3
	temp3 = otherHunter[0] * prey[0]
	temp3 = min( otherHunter[1] , temp5 )
	temp0 = -1 * dist
	temp4 = otherHunter[0] * otherHunter[0]
	temp3 = max( temp6 , temp1 )
	return [ prey[1] , temp4 ]
