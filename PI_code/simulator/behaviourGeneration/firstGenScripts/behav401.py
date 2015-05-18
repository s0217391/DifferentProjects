#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] * prey[1]
	temp1 = -1 * prey[1]
	temp2 = temp1 * temp1
	temp2 = prey[1] + temp1
	temp0 = -1 * prey[0]
	temp1 = -1 * temp2
	if temp1 > prey[0]:
		temp3 = -1 * temp2
	else:
		if temp0 != 0:
			temp3 = temp2 / temp0
		else:
			temp3 = temp0
	temp4 = min(temp2, prey[1])
	if prey[1] > temp2:
		if prey[1] != 0:
			temp4 = temp4 / prey[1]
		else:
			temp4 = prey[1]
	else:
		temp4 = temp4 + prey[1]
	temp4 = temp3 - temp1
	return [temp0, temp1]
