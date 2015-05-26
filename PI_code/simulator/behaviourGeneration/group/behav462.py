#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = otherHunter[1] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if otherHunter[0] != 0:
		temp1 = prey[1] / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	if otherHunter[0] > temp0 :
		temp1 = temp0 - prey[1]
	else:
		temp1 = dist - dist
	temp2 = min( temp0 , prey[0] )
	temp0 = otherHunter[1] + temp0
	temp1 = temp2 * temp2
	temp3 = min( otherHunter[1] , temp2 )
	temp1 = temp2 - dist
	temp1 = -1 * temp3
	if temp3 != 0:
		temp1 = prey[1] / temp3
	else:
		temp1 = temp3
	temp0 = max( prey[0] , otherHunter[1] )
	temp3 = otherHunter[1] * dist
	temp2 = prey[0] * temp0
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	if prey[1] != 0:
		temp0 = temp2 / prey[1]
	else:
		temp0 = prey[1]
	temp2 = -1 * prey[0]
	if temp0 != 0:
		temp0 = dist % temp0
	else:
		temp0 = temp0
	temp3 = temp0 * otherHunter[1]
	temp2 = otherHunter[0] + prey[1]
	return [ otherHunter[1] , otherHunter[0] ]
