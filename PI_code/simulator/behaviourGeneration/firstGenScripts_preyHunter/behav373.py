#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = max(prey[1], temp0)
	temp1 = -1 * prey[1]
	temp0 = prey[1] * prey[0]
	temp2 = prey[0] * temp0
	return [temp0, prey[0]]
