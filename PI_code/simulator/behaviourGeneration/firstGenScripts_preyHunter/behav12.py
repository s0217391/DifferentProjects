#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[0] - prey[1]
	temp0 = temp1 + temp0
	if prey[0] != 0:
		temp2 = temp0 / prey[0]
	else:
		temp2 = prey[0]
	temp0 = temp0 - prey[0]
	temp3 = max(temp0, temp0)
	temp1 = -1 * temp3
	temp3 = temp2 * prey[1]
	if temp3 > prey[0]:
		temp2 = temp0 - temp0
	else:
		temp2 = prey[0] + temp2
	temp1 = -1 * prey[0]
	temp1 = temp1 + temp2
	temp2 = prey[0] - prey[0]
	temp2 = prey[1] - temp3
	return [prey[1], temp3]