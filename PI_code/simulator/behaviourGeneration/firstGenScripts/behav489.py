#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = min(prey[1], prey[1])
	temp1 = prey[0] * temp0
	temp2 = min(prey[0], temp1)
	temp1 = temp1 + temp2
	return [prey[0], temp0]
