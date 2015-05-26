#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = -1 * prey[1]
	temp0 = temp0 - temp1
	temp0 = temp1 - prey[1]
	temp2 = min(temp1, prey[1])
	temp2 = min(temp2, temp2)
	return [temp0, prey[1]]
