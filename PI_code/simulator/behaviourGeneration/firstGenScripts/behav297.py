#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	if temp1 != 0:
		temp0 = prey[0] % temp1
	else:
		temp0 = temp1
	temp2 = -1 * temp1
	return [temp1, temp2]
