#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	temp1 = prey[0] - temp0
	temp1 = min(temp1, prey[0])
	if temp0 > prey[0]:
		temp1 = -1 * temp0
	else:
		temp1 = prey[1] * temp1
	temp0 = max(temp0, prey[0])
	if temp0 != 0:
		temp0 = temp1 / temp0
	else:
		temp0 = temp0
	temp2 = max(prey[0], temp1)
	temp3 = -1 * temp1
	temp1 = temp0 - prey[0]
	temp2 = max(prey[1], prey[1])
	temp2 = min(temp0, prey[0])
	temp4 = -1 * temp0
	temp4 = temp1 * temp4
	if temp0 != 0:
		temp5 = prey[1] % temp0
	else:
		temp5 = temp0
	temp1 = temp2 * temp2
	temp4 = temp0 - prey[1]
	if temp1 != 0:
		temp3 = prey[0] / temp1
	else:
		temp3 = temp1
	temp2 = min(temp3, temp5)
	if temp5 > temp0:
		temp5 = temp1 - temp2
	else:
		if temp3 != 0:
			temp5 = temp4 / temp3
		else:
			temp5 = temp3
	return [prey[1], temp4]
