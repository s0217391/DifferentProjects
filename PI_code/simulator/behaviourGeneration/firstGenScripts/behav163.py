#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = max(temp0, prey[1])
	temp0 = min(temp1, temp0)
	if prey[0] != 0:
		temp1 = temp1 % prey[0]
	else:
		temp1 = prey[0]
	return [temp1, temp0]
