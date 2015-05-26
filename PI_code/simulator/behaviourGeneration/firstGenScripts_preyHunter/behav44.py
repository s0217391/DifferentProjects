#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = max(prey[0], prey[1])
	temp2 = max(prey[1], temp1)
	return [prey[1], temp0]
