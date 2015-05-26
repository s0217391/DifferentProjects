#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[1])
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	if prey[0] != 0:
		temp1 = temp1 % prey[0]
	else:
		temp1 = prey[0]
	return [prey[1], prey[0]]
