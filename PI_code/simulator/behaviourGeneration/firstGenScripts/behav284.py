#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[0]
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = temp1 * prey[0]
	if temp1 > prey[0]:
		temp0 = max(prey[0], prey[1])
	else:
		if temp0 > prey[0]:
			if temp1 != 0:
				temp0 = temp1 % temp1
			else:
				temp0 = temp1
		else:
			temp0 = min(temp1, prey[0])
	temp2 = temp0 - prey[1]
	temp0 = temp0 - temp2
	if temp2 != 0:
		temp3 = temp0 / temp2
	else:
		temp3 = temp2
	temp2 = temp3 + prey[0]
	temp3 = prey[1] + prey[0]
	if prey[0] > temp2:
		temp3 = prey[0] - temp0
	else:
		if temp0 > temp0:
			if prey[0] != 0:
				temp3 = temp1 % prey[0]
			else:
				temp3 = prey[0]
		else:
			temp3 = min(temp3, prey[1])
	if temp2 != 0:
		temp3 = temp0 / temp2
	else:
		temp3 = temp2
	temp2 = prey[1] * temp2
	if temp3 != 0:
		temp1 = temp1 % temp3
	else:
		temp1 = temp3
	temp1 = -1 * prey[1]
	temp4 = min(prey[1], temp0)
	if temp1 != 0:
		temp0 = temp1 / temp1
	else:
		temp0 = temp1
	temp4 = temp4 + temp3
	temp1 = -1 * temp1
	return [prey[1], temp1]
