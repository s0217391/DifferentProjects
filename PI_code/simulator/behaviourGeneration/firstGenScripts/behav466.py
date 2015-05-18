#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[0]
	if prey[1] != 0:
		temp1 = temp0 % prey[1]
	else:
		temp1 = prey[1]
	temp2 = temp1 * prey[1]
	temp0 = -1 * prey[1]
	temp2 = temp0 + temp0
	temp3 = max(prey[0], prey[1])
	if prey[0] > temp0:
		temp3 = temp1 - temp3
	else:
		temp3 = -1 * temp0
	return [prey[1], temp1]
