#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	temp1 = max(prey[1], prey[0])
	temp1 = prey[1] + prey[0]
	if prey[1] != 0:
		temp2 = prey[1] % prey[1]
	else:
		temp2 = prey[1]
	temp3 = -1 * temp1
	return [temp0, prey[0]]
