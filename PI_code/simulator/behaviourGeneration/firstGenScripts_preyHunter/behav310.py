#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[1]
	if prey[0] != 0:
		temp1 = temp0 % prey[0]
	else:
		temp1 = prey[0]
	temp1 = max(temp0, prey[0])
	if prey[0] != 0:
		temp2 = temp1 / prey[0]
	else:
		temp2 = prey[0]
	return [temp2, prey[0]]