#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[1]:
		temp0 = prey[0] * prey[1]
	else:
		temp0 = -1 * prey[1]
	temp1 = min(prey[0], prey[0])
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	return [temp1, temp1]
