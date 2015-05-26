#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = -1 * temp0
	if temp0 != 0:
		temp0 = temp1 % temp0
	else:
		temp0 = temp0
	return [temp0, temp0]
