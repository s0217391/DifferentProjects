#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[0]:
		if prey[0] != 0:
			temp0 = prey[1] / prey[0]
		else:
			temp0 = prey[0]
	else:
		temp0 = min(prey[0], prey[1])
	temp1 = prey[0] * temp0
	temp1 = -1 * prey[0]
	temp1 = prey[0] + prey[1]
	temp0 = temp1 - prey[1]
	if temp1 != 0:
		temp1 = prey[0] / temp1
	else:
		temp1 = temp1
	return [temp0, temp1]
