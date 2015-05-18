#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	if prey[0] > prey[0]:
		temp1 = -1 * prey[1]
	else:
		temp1 = prey[0] * prey[0]
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	if temp0 > prey[0]:
		temp2 = min(temp0, temp1)
	else:
		temp2 = -1 * prey[1]
	temp2 = -1 * temp0
	if temp1 != 0:
		temp3 = prey[1] / temp1
	else:
		temp3 = temp1
	return [temp1, temp3]
