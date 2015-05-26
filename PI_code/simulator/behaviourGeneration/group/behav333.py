#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( otherHunter[1] , prey[0] )
	if otherHunter[1] != 0:
		temp1 = prey[1] % otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if otherHunter[0] > temp1 :
		temp2 = -1 * otherHunter[0]
	else:
		temp2 = -1 * prey[0]
	if temp0 != 0:
		temp1 = dist / temp0
	else:
		temp1 = temp0
	temp2 = dist * temp2
	if temp0 != 0:
		temp3 = otherHunter[1] % temp0
	else:
		temp3 = temp0
	temp3 = temp2 + prey[1]
	if otherHunter[0] > prey[0] :
		temp3 = prey[1] * otherHunter[1]
	else:
		temp3 = prey[1] + otherHunter[1]
	return [ temp2 , dist ]
