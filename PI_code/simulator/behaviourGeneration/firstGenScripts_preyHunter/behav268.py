#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[0])
	if prey[0] != 0:
		temp1 = prey[1] / prey[0]
	else:
		temp1 = prey[0]
	if prey[0] > prey[0]:
		temp2 = max(temp1, prey[1])
	else:
		temp2 = -1 * temp1
	temp2 = max(prey[0], prey[0])
	temp2 = temp2 * temp0
	temp2 = prey[1] - temp2
	if prey[0] != 0:
		temp2 = prey[0] / prey[0]
	else:
		temp2 = prey[0]
	return [prey[0], temp2]
