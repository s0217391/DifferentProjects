#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[1])
	temp1 = -1 * temp0
	temp2 = max(prey[1], prey[0])
	temp0 = -1 * temp2
	return [temp1, temp2]
