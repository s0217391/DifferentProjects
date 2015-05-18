#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	temp1 = temp0 * prey[0]
	temp0 = temp0 - prey[1]
	if prey[0] != 0:
		temp2 = prey[0] / prey[0]
	else:
		temp2 = prey[0]
	temp0 = -1 * prey[0]
	if prey[1] > prey[1]:
		temp3 = min(prey[1], temp0)
	else:
		temp3 = temp2 + prey[1]
	return [prey[0], prey[0]]
