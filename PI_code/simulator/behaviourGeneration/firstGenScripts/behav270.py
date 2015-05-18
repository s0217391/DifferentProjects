#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[0]:
		temp0 = prey[1] * prey[0]
	else:
		temp0 = -1 * prey[0]
	temp1 = prey[0] + temp0
	if prey[0] > temp1:
		temp0 = max(temp1, prey[0])
	else:
		temp0 = temp0 * prey[0]
	return [temp1, temp1]
