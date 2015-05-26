#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[0] != 0:
		temp0 = otherHunter[1] % otherHunter[0]
	else:
		temp0 = otherHunter[0]
	if otherHunter[1] > prey[0] :
		temp1 = min( prey[0] , prey[1] )
	else:
		temp1 = temp0 * temp0
	temp1 = temp1 + otherHunter[1]
	temp1 = otherHunter[1] - prey[0]
	temp1 = min( prey[1] , temp1 )
	if temp1 > temp0 :
		if temp0 != 0:
			temp0 = otherHunter[1] % temp0
		else:
			temp0 = temp0
	else:
		if temp1 > otherHunter[0] :
			temp0 = min( otherHunter[0] , otherHunter[0] )
		else:
			temp0 = otherHunter[1] + temp0
	return [ otherHunter[1] , prey[1] ]
