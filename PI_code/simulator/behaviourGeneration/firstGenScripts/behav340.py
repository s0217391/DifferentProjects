#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	temp1 = max(prey[0], prey[1])
	if temp1 > prey[1]:
		temp0 = temp1 - prey[1]
	else:
		if temp1 != 0:
			temp0 = prey[0] / temp1
		else:
			temp0 = temp1
	if prey[0] != 0:
		temp1 = prey[0] / prey[0]
	else:
		temp1 = prey[0]
	if temp1 > temp0:
		temp2 = prey[0] - temp0
	else:
		temp2 = prey[0] - temp1
	if temp0 > temp1:
		if prey[0] != 0:
			temp1 = temp1 / prey[0]
		else:
			temp1 = prey[0]
	else:
		temp1 = min(prey[0], prey[1])
	return [temp2, prey[1]]
