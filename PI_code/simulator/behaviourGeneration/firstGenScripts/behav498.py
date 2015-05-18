#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = prey[1] * prey[0]
	temp2 = temp1 * temp0
	if prey[0] != 0:
		temp0 = temp1 / prey[0]
	else:
		temp0 = prey[0]
	temp2 = temp1 * prey[0]
	temp1 = temp1 + temp1
	if temp1 != 0:
		temp2 = prey[0] % temp1
	else:
		temp2 = temp1
	temp3 = temp0 * temp0
	if temp0 != 0:
		temp4 = prey[1] / temp0
	else:
		temp4 = temp0
	return [prey[0], temp4]
