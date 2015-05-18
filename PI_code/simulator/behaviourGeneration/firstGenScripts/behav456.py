#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * prey[0]
	temp1 = prey[0] - temp1
	if prey[1] > prey[1]:
		temp1 = -1 * temp1
	else:
		temp1 = max(prey[1], temp0)
	temp2 = max(temp1, prey[1])
	temp2 = max(temp1, prey[1])
	if temp2 > temp0:
		if prey[1] != 0:
			temp0 = prey[0] / prey[1]
		else:
			temp0 = prey[1]
	else:
		temp0 = temp1 * prey[1]
	temp1 = temp1 + temp1
	temp1 = -1 * temp2
	if prey[1] != 0:
		temp1 = temp2 / prey[1]
	else:
		temp1 = prey[1]
	if temp2 != 0:
		temp2 = temp2 % temp2
	else:
		temp2 = temp2
	temp1 = max(temp0, prey[0])
	temp1 = temp0 - temp1
	temp0 = -1 * temp1
	temp2 = temp2 + prey[1]
	temp2 = prey[0] - prey[0]
	temp3 = max(temp2, temp1)
	temp4 = min(temp1, temp2)
	temp3 = max(temp2, temp3)
	temp4 = -1 * prey[0]
	temp4 = max(prey[0], temp0)
	temp5 = temp4 - temp4
	temp1 = -1 * temp1
	return [prey[1], temp0]
