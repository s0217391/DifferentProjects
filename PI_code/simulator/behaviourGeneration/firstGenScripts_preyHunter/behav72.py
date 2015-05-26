#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = prey[0] * prey[0]
	temp2 = min(temp1, prey[0])
	temp1 = temp2 + prey[0]
	temp1 = -1 * temp1
	temp0 = prey[1] - temp1
	temp0 = min(prey[0], prey[1])
	temp1 = max(temp2, prey[0])
	temp1 = prey[0] - temp0
	if temp1 != 0:
		temp3 = prey[0] / temp1
	else:
		temp3 = temp1
	return [temp0, temp1]
