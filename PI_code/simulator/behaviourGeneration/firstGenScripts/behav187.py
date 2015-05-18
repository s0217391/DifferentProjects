#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[1])
	temp1 = -1 * prey[1]
	temp0 = min(prey[1], temp1)
	temp1 = max(prey[0], temp0)
	temp2 = max(prey[0], temp1)
	temp3 = max(temp2, prey[0])
	temp4 = min(temp2, temp3)
	temp1 = -1 * temp3
	temp5 = max(temp1, prey[0])
	temp0 = -1 * temp0
	return [prey[0], temp0]
