#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[1]
	temp1 = -1 * temp0
	if temp1 != 0:
		temp1 = prey[0] % temp1
	else:
		temp1 = temp1
	temp1 = temp0 * prey[1]
	temp0 = max(prey[1], prey[0])
	temp0 = prey[1] - temp1
	temp2 = prey[0] - prey[1]
	temp1 = temp2 + temp2
	return [prey[1], temp0]
