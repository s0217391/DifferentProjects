#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = temp0 - temp0
	temp1 = max(prey[1], prey[1])
	temp1 = temp1 - temp1
	temp2 = -1 * temp1
	if temp2 != 0:
		temp1 = prey[0] / temp2
	else:
		temp1 = temp2
	temp2 = temp2 + prey[1]
	temp1 = min(temp1, temp1)
	temp3 = min(temp1, temp0)
	if prey[0] != 0:
		temp2 = prey[1] % prey[0]
	else:
		temp2 = prey[0]
	return [prey[0], prey[0]]
