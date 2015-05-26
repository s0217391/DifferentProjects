#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[0])
	temp1 = min(temp0, prey[0])
	if temp1 > prey[1]:
		temp1 = -1 * temp1
	else:
		temp1 = prey[0] * prey[1]
	temp0 = temp0 - prey[1]
	temp1 = temp1 - temp0
	temp0 = temp1 - prey[1]
	return [temp0, temp1]
