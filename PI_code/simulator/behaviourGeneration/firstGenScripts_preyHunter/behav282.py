#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[1]
	temp1 = prey[0] + prey[0]
	if temp1 != 0:
		temp0 = prey[0] % temp1
	else:
		temp0 = temp1
	return [prey[1], temp1]
