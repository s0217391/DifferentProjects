#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[1])
	temp1 = prey[0] + temp0
	temp2 = temp0 * temp0
	if temp1 > temp1:
		temp0 = max(prey[0], temp0)
	else:
		temp0 = min(prey[1], prey[0])
	if temp1 > temp2:
		if temp1 != 0:
			temp0 = prey[1] / temp1
		else:
			temp0 = temp1
	else:
		if temp1 != 0:
			temp0 = prey[1] / temp1
		else:
			temp0 = temp1
	temp3 = prey[0] * prey[1]
	if prey[1] > temp0:
		temp2 = -1 * temp2
	else:
		temp2 = min(prey[1], prey[0])
	temp3 = min(temp0, temp1)
	temp2 = prey[0] * temp0
	if temp1 != 0:
		temp1 = temp3 % temp1
	else:
		temp1 = temp1
	return [prey[1], prey[0]]
