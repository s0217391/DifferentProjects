#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * temp0
	temp0 = min( otherHunter[0] , otherHunter[1] )
	temp0 = max( otherHunter[1] , temp0 )
	if temp1 != 0:
		temp1 = otherHunter[1] / temp1
	else:
		temp1 = temp1
	if temp0 > prey[0] :
		if prey[1] != 0:
			temp1 = temp1 / prey[1]
		else:
			temp1 = prey[1]
	else:
		temp1 = prey[1] + dist
	temp1 = max( otherHunter[1] , prey[0] )
	if temp1 > dist :
		temp0 = temp0 + otherHunter[1]
	else:
		if otherHunter[0] > otherHunter[0] :
			if prey[1] > dist :
				temp0 = -1 * otherHunter[1]
			else:
				if temp0 != 0:
					temp0 = prey[1] / temp0
				else:
					temp0 = temp0
		else:
			temp0 = prey[1] * otherHunter[0]
	temp2 = max( otherHunter[0] , temp0 )
	temp0 = temp1 * dist
	if prey[1] != 0:
		temp2 = temp0 % prey[1]
	else:
		temp2 = prey[1]
	if temp1 != 0:
		temp2 = temp1 / temp1
	else:
		temp2 = temp1
	temp2 = temp1 - prey[0]
	temp1 = min( temp2 , prey[1] )
	temp1 = otherHunter[1] + otherHunter[1]
	if prey[1] != 0:
		temp3 = temp0 / prey[1]
	else:
		temp3 = prey[1]
	temp3 = min( prey[1] , temp3 )
	temp3 = prey[1] * otherHunter[0]
	temp1 = -1 * otherHunter[1]
	temp4 = -1 * temp0
	if otherHunter[0] > prey[0] :
		temp1 = temp4 - temp2
	else:
		if dist != 0:
			temp1 = otherHunter[1] % dist
		else:
			temp1 = dist
	temp4 = max( temp2 , otherHunter[1] )
	if prey[0] != 0:
		temp2 = dist / prey[0]
	else:
		temp2 = prey[0]
	return [ temp4 , temp2 ]
