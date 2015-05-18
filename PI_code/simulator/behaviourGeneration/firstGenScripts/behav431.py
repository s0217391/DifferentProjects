#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[0]
	temp1 = -1 * prey[0]
	temp2 = -1 * temp1
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	temp0 = -1 * temp1
	temp1 = max(prey[0], prey[1])
	temp1 = -1 * temp0
	temp3 = temp1 + temp1
	temp1 = max(prey[0], temp1)
	return [temp2, temp3]
