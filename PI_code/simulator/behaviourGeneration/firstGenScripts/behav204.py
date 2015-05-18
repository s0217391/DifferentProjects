#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[1]:
		if prey[1] > prey[0]:
			temp0 = prey[1] + prey[0]
		else:
			temp0 = min(prey[0], prey[1])
	else:
		temp0 = prey[0] * prey[1]
	temp1 = prey[1] + prey[1]
	temp2 = prey[1] + temp1
	temp1 = prey[0] * prey[1]
	temp3 = prey[1] + prey[0]
	return [temp2, prey[0]]
