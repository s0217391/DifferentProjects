#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	temp1 = min(prey[1], prey[1])
	temp1 = -1 * prey[1]
	temp2 = temp0 * prey[0]
	if temp0 != 0:
		temp2 = prey[0] / temp0
	else:
		temp2 = temp0
	temp0 = min(prey[1], prey[1])
	temp0 = temp2 * prey[1]
	temp1 = prey[1] * prey[0]
	temp1 = temp1 - prey[0]
	temp2 = max(temp1, temp2)
	temp3 = prey[0] + temp1
	temp3 = temp1 * prey[1]
	temp2 = temp0 + temp3
	return [temp0, prey[0]]
