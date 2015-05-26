#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		if prey[1] > prey[1]:
			temp0 = min(prey[1], prey[1])
		else:
			temp0 = max(prey[0], prey[1])
	else:
		temp0 = prey[1] * prey[1]
	temp1 = max(temp0, prey[1])
	temp2 = temp0 - temp1
	if temp2 != 0:
		temp3 = temp1 / temp2
	else:
		temp3 = temp2
	if temp3 != 0:
		temp2 = temp1 / temp3
	else:
		temp2 = temp3
	temp3 = min(prey[0], temp2)
	if temp1 != 0:
		temp0 = prey[1] % temp1
	else:
		temp0 = temp1
	temp4 = max(temp0, temp2)
	temp4 = max(prey[0], prey[1])
	return [temp3, temp0]
