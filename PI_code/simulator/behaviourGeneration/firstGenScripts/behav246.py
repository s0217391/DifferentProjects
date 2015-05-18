#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[1])
	temp1 = -1 * temp0
	if temp0 > prey[1]:
		if temp0 != 0:
			temp2 = temp1 / temp0
		else:
			temp2 = temp0
	else:
		temp2 = prey[1] - prey[0]
	if prey[0] != 0:
		temp2 = prey[0] / prey[0]
	else:
		temp2 = prey[0]
	temp1 = min(prey[1], temp2)
	return [prey[1], prey[1]]
