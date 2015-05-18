#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[1]
	temp1 = prey[0] * prey[1]
	temp0 = min(temp0, prey[1])
	if prey[0] > prey[1]:
		temp2 = min(temp0, prey[1])
	else:
		temp2 = prey[0] + prey[1]
	temp2 = temp2 + prey[0]
	temp3 = temp1 + temp1
	temp0 = max(temp0, temp0)
	temp0 = prey[0] + prey[1]
	if prey[0] > temp0:
		temp1 = max(temp3, prey[1])
	else:
		temp1 = prey[1] - temp3
	return [temp3, temp1]
