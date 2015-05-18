#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[0]
	if prey[0] != 0:
		temp1 = prey[0] % prey[0]
	else:
		temp1 = prey[0]
	temp0 = min(temp1, prey[0])
	return [temp0, temp0]
