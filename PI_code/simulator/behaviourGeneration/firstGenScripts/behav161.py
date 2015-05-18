#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[1])
	temp1 = max(temp0, prey[0])
	temp0 = prey[1] + prey[1]
	if temp1 > prey[0]:
		if prey[0] != 0:
			temp2 = temp0 / prey[0]
		else:
			temp2 = prey[0]
	else:
		temp2 = temp0 + prey[1]
	if temp2 != 0:
		temp0 = temp1 / temp2
	else:
		temp0 = temp2
	return [temp0, prey[0]]
