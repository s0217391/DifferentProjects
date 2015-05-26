#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[1]
	temp1 = prey[0] * prey[1]
	temp2 = temp0 * prey[1]
	if temp1 != 0:
		temp0 = temp0 % temp1
	else:
		temp0 = temp1
	if prey[0] != 0:
		temp1 = temp1 % prey[0]
	else:
		temp1 = prey[0]
	temp0 = temp0 * temp0
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	return [prey[0], prey[1]]
