#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[0]
	temp1 = prey[1] * prey[0]
	if prey[1] > prey[0]:
		temp2 = max(temp1, prey[1])
	else:
		temp2 = prey[1] + temp1
	temp2 = prey[1] - temp0
	temp1 = -1 * temp0
	return [temp1, temp2]
