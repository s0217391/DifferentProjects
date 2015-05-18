#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[1]:
		temp0 = prey[1] + prey[1]
	else:
		temp0 = prey[1] - prey[0]
	temp1 = prey[0] * prey[0]
	temp2 = temp1 * temp1
	return [temp1, temp2]
