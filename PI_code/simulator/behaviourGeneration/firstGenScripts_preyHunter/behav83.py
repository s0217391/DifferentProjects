#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[1])
	if temp0 != 0:
		temp1 = prey[1] % temp0
	else:
		temp1 = temp0
	temp0 = prey[1] * prey[0]
	temp1 = max(prey[0], prey[1])
	temp0 = max(temp0, prey[1])
	temp1 = -1 * prey[0]
	return [temp1, prey[1]]