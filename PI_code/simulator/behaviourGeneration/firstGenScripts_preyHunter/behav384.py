#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[1])
	temp1 = temp0 * temp0
	temp0 = -1 * prey[0]
	if temp0 != 0:
		temp0 = temp0 % temp0
	else:
		temp0 = temp0
	temp1 = prey[0] + prey[1]
	temp2 = prey[1] - prey[0]
	if temp0 != 0:
		temp0 = temp0 / temp0
	else:
		temp0 = temp0
	temp2 = temp1 - prey[1]
	temp2 = temp2 + temp1
	if prey[0] != 0:
		temp2 = temp1 % prey[0]
	else:
		temp2 = prey[0]
	temp3 = prey[0] + prey[1]
	if temp1 != 0:
		temp0 = temp2 / temp1
	else:
		temp0 = temp1
	temp0 = max(prey[1], temp0)
	if temp3 > prey[1]:
		if temp2 > prey[0]:
			temp1 = prey[1] * temp0
		else:
			temp1 = max(prey[1], temp1)
	else:
		temp1 = min(temp1, temp3)
	return [temp0, temp0]
