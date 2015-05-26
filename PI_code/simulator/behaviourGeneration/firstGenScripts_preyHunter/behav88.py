#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[1]
	temp1 = max(temp0, prey[1])
	if temp0 != 0:
		temp0 = prey[0] % temp0
	else:
		temp0 = temp0
	temp2 = prey[0] * temp0
	if temp2 != 0:
		temp1 = temp1 / temp2
	else:
		temp1 = temp2
	temp3 = -1 * prey[1]
	return [temp1, temp1]
