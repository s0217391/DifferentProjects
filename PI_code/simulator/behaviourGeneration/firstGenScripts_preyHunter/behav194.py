#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		temp0 = prey[1] * prey[1]
	else:
		temp0 = -1 * prey[0]
	if prey[0] > prey[1]:
		if temp0 > prey[0]:
			temp1 = -1 * temp0
		else:
			if prey[1] != 0:
				temp1 = prey[0] / prey[1]
			else:
				temp1 = prey[1]
	else:
		temp1 = max(temp0, temp0)
	if prey[0] > prey[0]:
		if temp0 != 0:
			temp0 = temp1 / temp0
		else:
			temp0 = temp0
	else:
		temp0 = temp0 - temp1
	temp2 = min(temp0, temp1)
	temp3 = min(prey[1], temp1)
	temp1 = prey[1] - temp0
	temp4 = max(temp3, temp1)
	if temp1 != 0:
		temp5 = temp3 / temp1
	else:
		temp5 = temp1
	temp2 = min(temp1, temp3)
	temp3 = temp1 + temp4
	temp4 = max(prey[0], temp0)
	if prey[0] != 0:
		temp3 = temp2 / prey[0]
	else:
		temp3 = prey[0]
	temp1 = temp1 * temp0
	if temp3 > temp5:
		temp2 = -1 * prey[1]
	else:
		if prey[1] != 0:
			temp2 = temp2 / prey[1]
		else:
			temp2 = prey[1]
	temp2 = -1 * temp4
	return [temp2, prey[0]]
