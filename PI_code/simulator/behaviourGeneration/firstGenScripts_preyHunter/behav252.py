#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[0])
	temp1 = prey[1] * prey[1]
	temp2 = -1 * temp1
	temp1 = temp2 - temp0
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	temp3 = temp1 - prey[0]
	if prey[1] != 0:
		temp2 = prey[1] / prey[1]
	else:
		temp2 = prey[1]
	temp3 = min(prey[0], temp2)
	temp2 = temp0 + temp2
	temp4 = temp3 + temp3
	temp5 = temp2 * temp1
	temp3 = temp3 * temp5
	temp1 = temp1 - temp2
	return [prey[0], temp1]
