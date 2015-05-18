#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[1]:
		temp0 = prey[0] - prey[1]
	else:
		temp0 = -1 * prey[1]
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	temp0 = -1 * temp0
	if temp1 > prey[1]:
		if prey[0] != 0:
			temp2 = prey[1] % prey[0]
		else:
			temp2 = prey[0]
	else:
		if temp1 > prey[0]:
			temp2 = min(temp0, temp0)
		else:
			temp2 = prey[1] + prey[0]
	temp0 = -1 * prey[1]
	temp3 = prey[0] * temp0
	temp0 = prey[0] - temp2
	temp3 = temp3 - temp0
	if prey[0] > temp2:
		temp2 = prey[1] - temp2
	else:
		if temp0 > temp0:
			temp2 = temp3 * temp2
		else:
			temp2 = temp2 + temp3
	temp1 = min(temp0, prey[0])
	if temp0 != 0:
		temp4 = temp3 / temp0
	else:
		temp4 = temp0
	temp0 = -1 * prey[0]
	if temp2 != 0:
		temp2 = temp2 % temp2
	else:
		temp2 = temp2
	return [prey[0], prey[1]]
