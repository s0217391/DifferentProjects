#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[0]
	if temp0 != 0:
		temp1 = prey[1] % temp0
	else:
		temp1 = temp0
	temp1 = max(prey[0], temp1)
	temp0 = -1 * temp0
	return [temp0, prey[1]]
