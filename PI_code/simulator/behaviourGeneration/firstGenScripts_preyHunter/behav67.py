#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[1])
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	if prey[1] > temp0:
		temp0 = max(temp0, temp1)
	else:
		temp0 = min(temp0, temp1)
	temp0 = prey[0] * prey[1]
	return [temp1, temp1]
