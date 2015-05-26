#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = min(temp0, prey[0])
	temp2 = temp1 * temp0
	temp0 = temp2 + temp2
	return [temp1, prey[1]]
