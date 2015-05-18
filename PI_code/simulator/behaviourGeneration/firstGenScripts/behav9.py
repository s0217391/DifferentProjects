#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	temp1 = prey[1] + temp0
	temp1 = max(prey[0], prey[0])
	temp0 = prey[1] + prey[1]
	temp0 = prey[1] * prey[0]
	temp1 = min(prey[1], temp1)
	temp1 = prey[0] - temp1
	if temp1 != 0:
		temp2 = prey[1] / temp1
	else:
		temp2 = temp1
	return [prey[0], prey[0]]
