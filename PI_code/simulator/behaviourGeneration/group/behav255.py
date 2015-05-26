#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[1] * prey[1]
	temp1 = prey[0] * otherHunter[1]
	if dist > prey[0] :
		temp0 = min( prey[0] , otherHunter[0] )
	else:
		if prey[1] != 0:
			temp0 = otherHunter[1] / prey[1]
		else:
			temp0 = prey[1]
	temp1 = -1 * prey[1]
	if otherHunter[1] != 0:
		temp1 = prey[0] / otherHunter[1]
	else:
		temp1 = otherHunter[1]
	if otherHunter[0] > temp0 :
		if temp1 != 0:
			temp2 = temp1 / temp1
		else:
			temp2 = temp1
	else:
		if prey[0] != 0:
			temp2 = prey[0] % prey[0]
		else:
			temp2 = prey[0]
	if prey[1] != 0:
		temp3 = prey[1] / prey[1]
	else:
		temp3 = prey[1]
	if temp3 > temp3 :
		temp3 = otherHunter[0] * prey[0]
	else:
		temp3 = dist + temp3
	temp2 = otherHunter[0] - prey[1]
	temp0 = otherHunter[1] * temp3
	temp2 = otherHunter[1] + prey[0]
	return [ otherHunter[1] , otherHunter[0] ]
