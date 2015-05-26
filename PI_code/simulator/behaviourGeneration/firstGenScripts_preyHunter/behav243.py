#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[1])
	temp1 = prey[1] + prey[0]
	if prey[1] > prey[0]:
		temp2 = min(prey[1], prey[0])
	else:
		temp2 = prey[0] * temp0
	temp3 = -1 * temp0
	if prey[0] > prey[1]:
		temp1 = prey[1] + prey[1]
	else:
		if temp1 > temp2:
			temp1 = min(temp1, temp3)
		else:
			if temp0 != 0:
				temp1 = temp2 % temp0
			else:
				temp1 = temp0
	temp1 = -1 * prey[1]
	if temp2 != 0:
		temp0 = temp1 % temp2
	else:
		temp0 = temp2
	if temp0 != 0:
		temp3 = temp2 / temp0
	else:
		temp3 = temp0
	if temp3 > temp0:
		temp2 = -1 * temp2
	else:
		temp2 = min(prey[0], temp3)
	temp0 = min(prey[0], temp1)
	return [temp3, prey[0]]
