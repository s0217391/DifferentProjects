#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = prey[1] - temp0
	temp0 = prey[0] * temp1
	temp0 = temp1 - temp1
	temp2 = -1 * prey[1]
	temp3 = max(temp0, prey[1])
	temp2 = temp3 * temp2
	temp3 = max(prey[0], temp0)
	return [prey[1], prey[1]]
