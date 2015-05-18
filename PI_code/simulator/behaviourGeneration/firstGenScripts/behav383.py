#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[1]
	temp1 = max(prey[0], temp0)
	if temp0 != 0:
		temp2 = prey[1] % temp0
	else:
		temp2 = temp0
	temp2 = -1 * prey[0]
	return [temp2, prey[0]]
