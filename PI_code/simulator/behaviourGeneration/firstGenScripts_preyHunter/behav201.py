#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] - prey[0]
	temp1 = prey[0] + prey[0]
	temp1 = prey[1] - prey[1]
	temp0 = min(prey[1], prey[0])
	return [prey[0], temp1]
