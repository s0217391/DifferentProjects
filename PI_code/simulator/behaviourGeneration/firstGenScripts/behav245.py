#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[0]:
		temp0 = prey[1] + prey[1]
	else:
		if prey[0] != 0:
			temp0 = prey[0] / prey[0]
		else:
			temp0 = prey[0]
	temp1 = prey[1] + temp0
	temp2 = min(temp0, prey[0])
	if temp0 > temp2:
		temp2 = temp2 - temp1
	else:
		temp2 = -1 * prey[1]
	temp0 = prey[0] - prey[1]
	if temp0 > temp0:
		temp0 = max(prey[0], temp0)
	else:
		if temp1 != 0:
			temp0 = prey[1] / temp1
		else:
			temp0 = temp1
	temp3 = prey[1] * temp2
	if temp0 != 0:
		temp0 = prey[0] % temp0
	else:
		temp0 = temp0
	temp2 = prey[0] - prey[1]
	temp4 = max(temp1, prey[0])
	temp1 = temp4 - temp4
	if temp4 != 0:
		temp3 = prey[1] / temp4
	else:
		temp3 = temp4
	temp0 = min(temp0, temp3)
	temp4 = temp1 + prey[1]
	temp4 = temp2 * temp0
	if prey[0] != 0:
		temp0 = temp3 / prey[0]
	else:
		temp0 = prey[0]
	temp1 = temp3 - temp2
	temp3 = min(temp1, temp3)
	temp1 = temp3 * temp3
	temp2 = max(temp1, temp1)
	temp0 = temp3 - temp0
	temp2 = temp3 * prey[1]
	if temp2 > prey[0]:
		temp5 = -1 * temp3
	else:
		temp5 = temp0 - temp4
	temp0 = -1 * temp0
	return [prey[0], temp5]
