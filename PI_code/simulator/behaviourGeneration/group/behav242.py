#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if otherHunter[1] != 0:
		temp0 = prey[1] % otherHunter[1]
	else:
		temp0 = otherHunter[1]
	if prey[0] != 0:
		temp1 = prey[1] / prey[0]
	else:
		temp1 = prey[0]
	temp1 = dist - prey[1]
	temp1 = max( otherHunter[1] , prey[0] )
	if temp0 != 0:
		temp2 = prey[1] / temp0
	else:
		temp2 = temp0
	temp2 = min( prey[0] , prey[0] )
	if otherHunter[0] != 0:
		temp1 = temp1 / otherHunter[0]
	else:
		temp1 = otherHunter[0]
	temp0 = otherHunter[0] * prey[0]
	temp1 = max( temp0 , otherHunter[0] )
	if temp0 > prey[0] :
		temp3 = temp2 - otherHunter[0]
	else:
		if temp1 != 0:
			temp3 = temp0 / temp1
		else:
			temp3 = temp1
	temp2 = -1 * dist
	temp0 = prey[0] * otherHunter[1]
	if prey[1] > otherHunter[0] :
		if temp1 > otherHunter[1] :
			if dist != 0:
				temp2 = otherHunter[1] % dist
			else:
				temp2 = dist
		else:
			if prey[0] > prey[0] :
				temp2 = max( temp1 , prey[0] )
			else:
				if otherHunter[1] > temp0 :
					temp2 = min( temp3 , otherHunter[0] )
				else:
					temp2 = otherHunter[0] * dist
	else:
		temp2 = temp0 * dist
	if temp0 > temp2 :
		temp0 = temp2 + prey[1]
	else:
		temp0 = min( temp2 , temp2 )
	temp4 = min( prey[0] , prey[0] )
	temp3 = otherHunter[1] * otherHunter[0]
	temp2 = prey[1] - prey[1]
	if temp0 > temp2 :
		temp5 = min( otherHunter[1] , otherHunter[1] )
	else:
		temp5 = temp3 * otherHunter[0]
	return [ temp3 , temp5 ]
