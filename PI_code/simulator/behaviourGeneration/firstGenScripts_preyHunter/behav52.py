#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[1])
	temp1 = -1 * temp0
	temp2 = max(temp0, temp1)
	temp1 = -1 * prey[0]
	temp1 = max(prey[0], prey[1])
	temp3 = -1 * prey[0]
	temp3 = min(temp0, temp3)
	if temp1 > temp3:
		temp4 = max(temp0, prey[1])
	else:
		temp4 = -1 * temp3
	return [prey[1], temp1]
