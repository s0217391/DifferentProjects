#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	if prey[0] > temp0:
		temp1 = -1 * prey[1]
	else:
		temp1 = min(temp0, prey[1])
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	temp2 = prey[0] + temp0
	temp3 = min(temp2, temp2)
	return [temp0, temp0]
