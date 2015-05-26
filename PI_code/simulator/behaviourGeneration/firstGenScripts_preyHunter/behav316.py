#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[0])
	temp1 = prey[0] * prey[0]
	temp0 = max(prey[0], temp1)
	temp1 = min(prey[1], temp0)
	if prey[0] > prey[0]:
		temp0 = prey[0] * prey[0]
	else:
		temp0 = min(temp1, prey[0])
	if temp1 > temp1:
		temp2 = max(temp1, prey[1])
	else:
		temp2 = prey[1] - temp0
	if prey[1] > temp1:
		temp1 = -1 * prey[0]
	else:
		temp1 = -1 * prey[0]
	temp3 = min(temp1, prey[0])
	temp1 = prey[1] + temp2
	temp4 = min(prey[0], temp3)
	temp2 = max(temp3, prey[1])
	temp2 = temp4 + prey[1]
	return [temp0, temp2]
