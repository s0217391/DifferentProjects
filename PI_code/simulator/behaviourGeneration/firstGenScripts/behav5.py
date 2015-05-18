#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	temp1 = -1 * temp0
	temp0 = max(prey[0], prey[0])
	if temp1 > prey[1]:
		if temp1 != 0:
			temp2 = prey[0] / temp1
		else:
			temp2 = temp1
	else:
		if temp0 != 0:
			temp2 = prey[1] / temp0
		else:
			temp2 = temp0
	temp0 = -1 * temp0
	temp1 = -1 * temp2
	temp3 = max(temp0, prey[0])
	if prey[0] > prey[1]:
		temp1 = max(temp0, prey[1])
	else:
		temp1 = min(temp1, temp0)
	return [prey[1], temp3]
