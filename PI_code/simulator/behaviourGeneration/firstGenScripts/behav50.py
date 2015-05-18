#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[0])
	temp1 = prey[1] + prey[0]
	if temp0 > prey[0]:
		temp1 = prey[1] - prey[1]
	else:
		temp1 = min(temp0, temp0)
	temp2 = temp0 - prey[0]
	return [temp0, prey[1]]
