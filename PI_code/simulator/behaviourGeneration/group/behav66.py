#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] * otherHunter[0]
	temp1 = min( temp0 , otherHunter[1] )
	if prey[0] != 0:
		temp0 = otherHunter[1] / prey[0]
	else:
		temp0 = prey[0]
	if prey[0] > dist :
		temp2 = min( temp1 , otherHunter[0] )
	else:
		temp2 = max( temp0 , otherHunter[0] )
	if prey[1] != 0:
		temp3 = otherHunter[0] % prey[1]
	else:
		temp3 = prey[1]
	temp4 = otherHunter[1] + prey[1]
	temp0 = -1 * temp4
	temp1 = temp2 * prey[1]
	temp3 = temp3 + otherHunter[0]
	temp5 = temp2 - temp2
	temp4 = -1 * temp5
	if prey[1] != 0:
		temp6 = temp0 / prey[1]
	else:
		temp6 = prey[1]
	return [ otherHunter[1] , temp1 ]
