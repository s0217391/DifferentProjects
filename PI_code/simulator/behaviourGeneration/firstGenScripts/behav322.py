#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[0]
	temp1 = -1 * temp0
	temp1 = min(temp1, temp1)
	temp2 = -1 * temp0
	temp3 = max(prey[1], temp1)
	if prey[1] > temp3:
		if temp3 > temp1:
			temp4 = -1 * prey[1]
		else:
			temp4 = temp3 * temp0
	else:
		if prey[1] > prey[0]:
			temp4 = -1 * prey[0]
		else:
			temp4 = -1 * temp2
	temp0 = temp4 + temp4
	temp5 = max(temp1, temp2)
	temp2 = temp1 * temp5
	return [temp3, temp2]
