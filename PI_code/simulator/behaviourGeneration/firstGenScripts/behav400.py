#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = temp0 + prey[1]
	temp0 = temp1 - temp0
	return [prey[0], temp1]
