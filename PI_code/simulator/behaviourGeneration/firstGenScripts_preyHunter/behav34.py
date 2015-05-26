#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = -1 * prey[1]
	temp1 = max(temp0, temp1)
	temp1 = temp0 * prey[1]
	temp2 = min(temp1, temp0)
	temp0 = temp2 + prey[1]
	temp2 = prey[0] - prey[1]
	temp2 = prey[0] * prey[0]
	if prey[0] != 0:
		temp3 = prey[0] % prey[0]
	else:
		temp3 = prey[0]
	temp1 = temp1 + prey[1]
	temp2 = max(temp1, prey[1])
	temp0 = max(temp2, temp3)
	temp0 = max(prey[1], temp2)
	temp0 = max(prey[0], temp1)
	temp3 = max(temp1, temp3)
	temp4 = max(temp0, prey[1])
	return [prey[1], temp2]
