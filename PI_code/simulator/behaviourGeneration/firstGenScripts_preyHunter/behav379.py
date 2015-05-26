#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[0] + prey[0]
	temp2 = max(temp1, temp1)
	return [prey[1], temp2]
