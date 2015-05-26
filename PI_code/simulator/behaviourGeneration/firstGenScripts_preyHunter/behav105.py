#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[1]:
		if prey[0] > prey[0]:
			if prey[1] != 0:
				temp0 = prey[1] / prey[1]
			else:
				temp0 = prey[1]
		else:
			temp0 = min(prey[1], prey[0])
	else:
		temp0 = max(prey[0], prey[1])
	temp1 = prey[0] + temp0
	temp1 = -1 * temp1
	if temp0 > temp0:
		if temp1 != 0:
			temp0 = temp0 / temp1
		else:
			temp0 = temp1
	else:
		temp0 = temp0 + prey[0]
	temp0 = prey[0] - temp1
	if temp0 != 0:
		temp1 = temp0 % temp0
	else:
		temp1 = temp0
	if temp1 > temp1:
		temp0 = max(temp0, prey[0])
	else:
		temp0 = -1 * prey[1]
	temp1 = temp0 + temp0
	if temp0 != 0:
		temp0 = prey[0] / temp0
	else:
		temp0 = temp0
	temp2 = prey[0] - prey[1]
	temp0 = prey[1] * temp1
	temp0 = max(temp0, prey[0])
	temp1 = temp0 + temp0
	temp3 = max(prey[1], temp1)
	temp3 = temp2 * prey[0]
	temp4 = max(temp1, prey[0])
	if prey[1] > temp3:
		temp2 = temp1 * temp2
	else:
		temp2 = temp3 - temp1
	temp4 = temp1 + temp0
	temp2 = -1 * temp4
	temp3 = prey[0] * prey[1]
	temp5 = prey[1] * prey[1]
	if temp2 > prey[1]:
		temp5 = prey[0] + prey[1]
	else:
		temp5 = temp5 * prey[1]
	temp2 = prey[0] + temp5
	if temp1 != 0:
		temp2 = temp3 / temp1
	else:
		temp2 = temp1
	temp5 = -1 * temp5
	return [temp2, temp5]
