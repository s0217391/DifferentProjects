#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = temp0 + prey[1]
	if prey[0] > temp1:
		temp1 = min(prey[1], prey[1])
	else:
		temp1 = min(temp1, prey[1])
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	return [prey[1], prey[0]]
