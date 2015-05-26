#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = min( prey[1] , prey[1] )
	temp1 = -1 * otherHunter[1]
	if dist != 0:
		temp1 = dist / dist
	else:
		temp1 = dist
	temp1 = prey[0] + prey[0]
	temp1 = dist * dist
	temp2 = prey[1] + prey[1]
	temp1 = temp2 + otherHunter[1]
	if otherHunter[0] != 0:
		temp0 = temp2 / otherHunter[0]
	else:
		temp0 = otherHunter[0]
	temp1 = -1 * temp2
	if temp2 > prey[0] :
		temp3 = -1 * temp0
	else:
		temp3 = -1 * temp0
	if otherHunter[1] > prey[1] :
		temp2 = max( temp3 , temp1 )
	else:
		temp2 = otherHunter[0] - temp0
	if temp0 != 0:
		temp0 = otherHunter[1] % temp0
	else:
		temp0 = temp0
	temp0 = prey[0] - temp2
	temp2 = temp3 - prey[0]
	if prey[0] > temp2 :
		temp1 = temp0 + temp3
	else:
		temp1 = -1 * prey[1]
	temp1 = prey[0] - temp3
	if prey[0] > temp0 :
		temp1 = max( otherHunter[0] , prey[0] )
	else:
		temp1 = min( temp3 , otherHunter[0] )
	temp0 = prey[1] * temp2
	temp3 = max( otherHunter[1] , otherHunter[0] )
	if temp1 != 0:
		temp4 = temp2 / temp1
	else:
		temp4 = temp1
	temp0 = otherHunter[1] - prey[0]
	return [ temp2 , temp4 ]
