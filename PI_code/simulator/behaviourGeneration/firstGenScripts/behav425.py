#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[0]:
		temp0 = prey[1] * prey[1]
	else:
		temp0 = prey[0] - prey[0]
	temp1 = -1 * temp0
	if prey[1] > temp0:
		temp1 = min(prey[1], temp0)
	else:
		if temp0 != 0:
			temp1 = temp0 / temp0
		else:
			temp1 = temp0
	temp0 = temp1 * temp0
	temp0 = -1 * temp0
	temp1 = min(prey[1], prey[1])
	temp1 = prey[0] - temp0
	temp0 = temp1 * temp1
	temp1 = min(temp1, temp1)
	temp1 = max(prey[1], temp1)
	temp0 = temp0 + prey[0]
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	temp0 = min(prey[0], temp1)
	temp2 = prey[1] + temp1
	temp3 = prey[1] - prey[0]
	return [prey[0], temp2]
