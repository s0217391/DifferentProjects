#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	temp1 = min(prey[1], prey[1])
	if temp1 != 0:
		temp1 = temp1 / temp1
	else:
		temp1 = temp1
	temp0 = min(temp0, temp0)
	temp0 = prey[0] * prey[1]
	temp1 = max(temp0, temp1)
	temp0 = prey[0] * prey[1]
	return [temp1, temp0]
