#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[1]
	if prey[0] != 0:
		temp1 = temp0 % prey[0]
	else:
		temp1 = prey[0]
	temp2 = -1 * prey[1]
	temp0 = temp1 - prey[1]
	if prey[1] > prey[1]:
		if temp0 > prey[0]:
			temp2 = temp1 * prey[0]
		else:
			temp2 = prey[1] - temp2
	else:
		temp2 = temp0 + prey[1]
	temp0 = temp2 * prey[1]
	temp2 = min(temp0, temp2)
	if prey[0] != 0:
		temp1 = temp2 % prey[0]
	else:
		temp1 = prey[0]
	temp0 = temp0 - temp1
	temp1 = -1 * temp1
	temp0 = temp1 + temp1
	temp1 = prey[1] + temp0
	temp1 = min(temp0, prey[1])
	temp2 = prey[0] * temp0
	if temp2 != 0:
		temp2 = temp0 % temp2
	else:
		temp2 = temp2
	temp0 = prey[1] + temp2
	temp3 = min(temp1, temp0)
	temp1 = max(temp0, temp3)
	return [prey[1], temp0]
