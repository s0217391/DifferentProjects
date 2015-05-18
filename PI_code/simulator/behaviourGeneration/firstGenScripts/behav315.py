#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[1]
	temp1 = max(prey[1], prey[0])
	temp0 = prey[1] + prey[1]
	temp2 = max(prey[0], prey[1])
	if prey[0] != 0:
		temp3 = temp1 / prey[0]
	else:
		temp3 = prey[0]
	temp2 = -1 * prey[0]
	temp0 = max(temp0, prey[0])
	return [temp1, temp0]
