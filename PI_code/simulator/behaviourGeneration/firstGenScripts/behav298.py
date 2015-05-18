#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = temp0 - prey[1]
	temp1 = temp1 * temp0
	temp1 = -1 * prey[1]
	temp1 = max(temp1, prey[1])
	temp0 = min(temp1, temp1)
	temp1 = min(temp0, temp1)
	temp2 = prey[0] * temp0
	temp1 = max(prey[0], temp2)
	if temp1 != 0:
		temp1 = temp1 / temp1
	else:
		temp1 = temp1
	temp0 = min(temp0, temp1)
	temp0 = -1 * prey[1]
	temp1 = prey[1] - prey[0]
	temp1 = prey[0] + temp0
	temp1 = min(temp1, temp2)
	return [temp0, prey[1]]
