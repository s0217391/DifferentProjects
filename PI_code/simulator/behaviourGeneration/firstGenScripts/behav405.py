#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[0])
	temp1 = min(temp0, prey[1])
	temp1 = prey[0] - temp0
	temp1 = prey[1] - prey[1]
	temp2 = max(prey[0], temp1)
	return [temp1, temp2]
