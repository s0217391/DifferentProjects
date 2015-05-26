#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * temp0
	if temp1 != 0:
		temp1 = temp1 % temp1
	else:
		temp1 = temp1
	temp0 = min(temp1, prey[0])
	temp1 = min(temp1, temp0)
	return [prey[1], prey[0]]
