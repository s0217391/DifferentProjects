#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * temp0
	temp1 = prey[0] - prey[0]
	temp2 = temp0 - temp0
	if prey[0] != 0:
		temp2 = prey[0] / prey[0]
	else:
		temp2 = prey[0]
	temp2 = prey[0] * prey[1]
	temp3 = -1 * temp2
	if prey[1] != 0:
		temp0 = temp0 / prey[1]
	else:
		temp0 = prey[1]
	if temp1 != 0:
		temp4 = prey[1] / temp1
	else:
		temp4 = temp1
	temp2 = temp1 * temp4
	return [prey[1], temp4]
