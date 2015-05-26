#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = dist % prey[1]
	else:
		temp0 = prey[1]
	temp1 = max( otherHunter[1] , prey[0] )
	if temp1 != 0:
		temp1 = prey[0] % temp1
	else:
		temp1 = temp1
	if temp0 != 0:
		temp0 = otherHunter[0] / temp0
	else:
		temp0 = temp0
	if otherHunter[0] > otherHunter[0] :
		if otherHunter[0] > temp1 :
			if otherHunter[0] > prey[1] :
				if temp1 != 0:
					temp2 = temp0 % temp1
				else:
					temp2 = temp1
			else:
				if temp0 != 0:
					temp2 = temp0 % temp0
				else:
					temp2 = temp0
		else:
			if temp0 != 0:
				temp2 = otherHunter[0] % temp0
			else:
				temp2 = temp0
	else:
		temp2 = max( otherHunter[1] , prey[1] )
	return [ temp1 , temp0 ]
