#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[0])
	if temp0 != 0:
		temp1 = temp0 / temp0
	else:
		temp1 = temp0
	temp0 = prey[1] * prey[1]
	if prey[1] > temp0:
		temp2 = max(prey[1], temp1)
	else:
		temp2 = max(prey[1], temp1)
	if temp0 > temp1:
		temp3 = max(prey[0], temp2)
	else:
		if temp0 != 0:
			temp3 = temp1 / temp0
		else:
			temp3 = temp0
	return [temp2, temp3]
