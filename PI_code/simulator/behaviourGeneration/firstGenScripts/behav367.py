#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp1 = prey[0] - prey[0]
	temp2 = prey[0] - prey[0]
	temp0 = prey[1] * temp2
	return [temp2, temp1]
