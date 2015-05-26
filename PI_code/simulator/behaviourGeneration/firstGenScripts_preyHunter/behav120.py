#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[1]
	temp1 = min(prey[1], temp0)
	if temp0 > prey[1]:
		temp0 = min(temp0, prey[0])
	else:
		temp0 = prey[1] + temp0
	temp0 = temp1 * prey[1]
	temp1 = prey[0] - prey[0]
	temp0 = temp0 * prey[1]
	temp0 = -1 * temp0
	temp1 = max(temp1, prey[0])
	temp0 = -1 * temp0
	temp2 = temp1 - prey[0]
	temp1 = max(temp0, temp2)
	temp2 = min(prey[1], temp2)
	temp0 = temp2 + prey[0]
	if prey[1] > prey[0]:
		temp0 = max(temp0, prey[1])
	else:
		if prey[1] != 0:
			temp0 = prey[0] / prey[1]
		else:
			temp0 = prey[1]
	if temp2 != 0:
		temp2 = prey[0] / temp2
	else:
		temp2 = temp2
	temp2 = prey[0] + temp2
	temp0 = -1 * prey[1]
	temp0 = temp0 * temp2
	temp3 = max(temp2, prey[0])
	temp2 = -1 * temp2
	temp4 = max(temp3, temp3)
	temp2 = max(temp2, prey[1])
	temp3 = prey[0] * prey[0]
	temp2 = max(temp2, temp0)
	return [temp4, prey[0]]
