#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	temp1 = temp0 + temp0
	if temp1 != 0:
		temp0 = prey[1] % temp1
	else:
		temp0 = temp1
	temp0 = min(temp1, temp1)
	if prey[1] != 0:
		temp1 = prey[0] % prey[1]
	else:
		temp1 = prey[1]
	temp0 = prey[0] - prey[1]
	temp1 = prey[1] * prey[1]
	temp0 = min(prey[1], temp0)
	temp2 = temp0 + temp1
	if prey[1] > prey[1]:
		if temp0 != 0:
			temp0 = prey[0] % temp0
		else:
			temp0 = temp0
	else:
		if temp2 != 0:
			temp0 = temp2 % temp2
		else:
			temp0 = temp2
	temp0 = prey[1] - temp1
	temp0 = prey[0] * prey[1]
	temp3 = min(temp1, prey[1])
	temp2 = prey[1] - temp3
	temp4 = min(temp3, temp1)
	temp5 = min(temp2, temp2)
	return [prey[0], temp3]
