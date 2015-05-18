#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = max(prey[0], prey[0])
	if prey[1] > prey[0]:
		if temp1 > temp0:
			temp2 = temp1 * prey[0]
		else:
			temp2 = temp0 * temp0
	else:
		temp2 = prey[0] - prey[1]
	temp1 = temp2 - prey[0]
	temp0 = max(temp2, temp0)
	temp3 = -1 * temp0
	if temp1 > temp1:
		temp4 = min(temp3, prey[0])
	else:
		temp4 = -1 * temp0
	temp3 = max(prey[0], temp2)
	temp4 = temp0 * temp1
	if temp4 != 0:
		temp5 = temp2 / temp4
	else:
		temp5 = temp4
	temp0 = max(prey[0], temp1)
	temp0 = prey[1] * prey[1]
	if temp0 > prey[0]:
		temp5 = max(temp0, temp4)
	else:
		temp5 = temp1 - temp0
	temp5 = temp3 - prey[1]
	temp4 = -1 * prey[0]
	temp5 = prey[1] - prey[0]
	temp1 = temp4 + temp0
	temp2 = temp3 + temp1
	return [prey[0], temp4]
