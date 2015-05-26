#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[0], prey[0])
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	temp0 = temp1 + temp0
	temp2 = prey[1] * temp0
	temp1 = prey[1] + temp1
	if prey[0] != 0:
		temp3 = temp2 % prey[0]
	else:
		temp3 = prey[0]
	temp3 = min(prey[1], temp3)
	if temp0 > prey[0]:
		temp3 = max(prey[1], temp1)
	else:
		temp3 = min(temp3, temp3)
	temp1 = min(prey[0], prey[0])
	temp2 = -1 * prey[1]
	if temp3 > temp1:
		temp0 = min(temp0, temp0)
	else:
		temp0 = -1 * prey[1]
	temp0 = temp2 + prey[0]
	temp1 = min(temp0, temp1)
	temp2 = prey[1] * prey[0]
	temp1 = prey[0] * temp2
	temp0 = prey[1] - temp2
	return [temp3, temp1]
