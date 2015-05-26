#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[0])
	temp1 = max(prey[0], temp0)
	temp0 = min(temp0, temp1)
	if temp1 != 0:
		temp2 = prey[1] / temp1
	else:
		temp2 = temp1
	if prey[1] > temp2:
		temp3 = prey[1] * prey[0]
	else:
		temp3 = prey[0] - prey[0]
	temp4 = temp0 - temp0
	temp4 = temp3 * prey[1]
	temp2 = temp0 + prey[0]
	temp2 = temp0 - temp3
	return [prey[1], temp1]
