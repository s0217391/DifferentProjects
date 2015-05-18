#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = min(temp0, temp0)
	temp2 = min(temp1, prey[0])
	temp3 = min(temp2, temp1)
	if temp3 != 0:
		temp0 = temp1 / temp3
	else:
		temp0 = temp3
	temp2 = -1 * temp0
	return [temp0, prey[0]]
