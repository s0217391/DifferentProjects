#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[1])
	temp1 = temp0 * prey[0]
	temp2 = min(prey[0], temp0)
	if temp0 != 0:
		temp2 = temp1 / temp0
	else:
		temp2 = temp0
	temp2 = min(temp2, prey[1])
	temp0 = temp2 + temp2
	temp2 = temp1 - prey[0]
	temp1 = max(temp2, temp1)
	temp1 = temp2 + temp0
	if prey[1] > temp2:
		temp1 = -1 * temp0
	else:
		if temp1 > temp1:
			temp1 = max(temp0, temp0)
		else:
			if prey[1] != 0:
				temp1 = temp0 % prey[1]
			else:
				temp1 = prey[1]
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	return [prey[1], prey[1]]
