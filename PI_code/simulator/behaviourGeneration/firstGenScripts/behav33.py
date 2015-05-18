#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[1]
	temp1 = temp0 + temp0
	temp2 = min(temp1, prey[0])
	if temp2 > prey[0]:
		temp2 = prey[0] - prey[0]
	else:
		temp2 = prey[1] + prey[1]
	return [prey[0], temp1]
