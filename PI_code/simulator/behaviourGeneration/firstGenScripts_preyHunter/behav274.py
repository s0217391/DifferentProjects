#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	if prey[1] > prey[1]:
		if temp0 > prey[0]:
			temp1 = temp0 - prey[1]
		else:
			temp1 = prey[1] - prey[0]
	else:
		if prey[0] != 0:
			temp1 = prey[0] / prey[0]
		else:
			temp1 = prey[0]
	temp1 = max(prey[1], prey[0])
	temp0 = max(temp0, prey[1])
	if temp0 > prey[1]:
		if prey[1] > prey[0]:
			temp1 = temp0 * temp1
		else:
			if temp1 != 0:
				temp1 = temp0 % temp1
			else:
				temp1 = temp1
	else:
		temp1 = max(temp1, temp1)
	temp2 = max(prey[1], prey[1])
	if temp0 != 0:
		temp2 = temp1 % temp0
	else:
		temp2 = temp0
	return [prey[1], temp0]
