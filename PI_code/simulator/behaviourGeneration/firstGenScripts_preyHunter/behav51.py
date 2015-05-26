#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[0]
	temp1 = prey[0] + temp0
	temp2 = -1 * prey[0]
	temp3 = temp2 * temp1
	if temp2 != 0:
		temp4 = temp0 % temp2
	else:
		temp4 = temp2
	temp1 = temp4 * temp2
	if prey[1] != 0:
		temp1 = temp2 % prey[1]
	else:
		temp1 = prey[1]
	if temp3 != 0:
		temp2 = temp2 / temp3
	else:
		temp2 = temp3
	temp5 = max(temp3, prey[0])
	temp3 = max(temp0, prey[0])
	if temp5 != 0:
		temp0 = temp4 / temp5
	else:
		temp0 = temp5
	temp5 = temp1 * prey[0]
	temp1 = prey[1] + temp5
	temp6 = max(temp1, temp1)
	return [temp1, prey[0]]
