#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = prey[0] * dist
	if prey[0] > prey[1] :
		temp1 = prey[1] + otherHunter[1]
	else:
		temp1 = prey[0] * temp0
	if prey[0] > dist :
		temp0 = otherHunter[1] * dist
	else:
		if prey[0] > temp1 :
			temp0 = min( dist , otherHunter[0] )
		else:
			if temp0 > dist :
				temp0 = min( temp0 , prey[1] )
			else:
				if prey[0] != 0:
					temp0 = temp1 / prey[0]
				else:
					temp0 = prey[0]
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	if otherHunter[1] > prey[0] :
		if prey[0] > otherHunter[0] :
			temp2 = otherHunter[0] * otherHunter[1]
		else:
			temp2 = temp1 - temp1
	else:
		temp2 = temp0 - otherHunter[0]
	temp0 = temp2 - temp1
	if prey[1] != 0:
		temp1 = prey[1] % prey[1]
	else:
		temp1 = prey[1]
	temp1 = dist + otherHunter[1]
	temp3 = temp0 * temp1
	if temp2 != 0:
		temp3 = prey[1] / temp2
	else:
		temp3 = temp2
	temp0 = temp0 - otherHunter[0]
	if prey[0] != 0:
		temp0 = temp3 % prey[0]
	else:
		temp0 = prey[0]
	temp2 = min( prey[0] , otherHunter[0] )
	if temp0 != 0:
		temp3 = otherHunter[1] / temp0
	else:
		temp3 = temp0
	temp3 = min( temp1 , temp3 )
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	temp1 = -1 * otherHunter[0]
	if temp2 > otherHunter[0] :
		temp4 = max( temp3 , otherHunter[0] )
	else:
		temp4 = otherHunter[1] - temp1
	temp3 = min( temp3 , otherHunter[0] )
	return [ prey[0] , prey[0] ]
