#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[0]
	temp1 = max(prey[1], prey[0])
	temp2 = min(prey[1], prey[0])
	if temp1 != 0:
		temp2 = temp0 / temp1
	else:
		temp2 = temp1
	temp2 = -1 * prey[0]
	temp0 = -1 * prey[0]
	temp0 = temp0 * prey[1]
	if prey[0] != 0:
		temp3 = temp2 % prey[0]
	else:
		temp3 = prey[0]
	return [prey[1], temp3]
