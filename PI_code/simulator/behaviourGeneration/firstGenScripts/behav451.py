#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = -1 * prey[1]
	if temp0 != 0:
		temp2 = prey[0] % temp0
	else:
		temp2 = temp0
	if temp1 != 0:
		temp1 = prey[1] % temp1
	else:
		temp1 = temp1
	temp0 = temp1 - temp0
	return [temp2, prey[0]]
