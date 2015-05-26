#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	if temp1 != 0:
		temp0 = temp0 % temp1
	else:
		temp0 = temp1
	if temp1 != 0:
		temp0 = temp0 % temp1
	else:
		temp0 = temp1
	temp0 = max(prey[1], prey[1])
	temp2 = prey[0] + temp1
	temp1 = prey[1] - temp1
	return [temp2, temp1]
