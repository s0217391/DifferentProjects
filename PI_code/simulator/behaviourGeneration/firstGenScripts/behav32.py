#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[1]
	temp1 = prey[1] * prey[0]
	temp0 = max(prey[1], prey[0])
	return [temp1, prey[0]]
