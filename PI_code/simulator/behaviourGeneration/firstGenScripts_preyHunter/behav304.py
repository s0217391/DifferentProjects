#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	temp1 = -1 * prey[1]
	temp1 = min(temp1, temp0)
	return [temp0, prey[1]]
