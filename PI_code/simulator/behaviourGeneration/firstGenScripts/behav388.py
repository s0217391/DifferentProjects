#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[1]
	if temp0 > prey[0]:
		temp1 = min(temp0, temp0)
	else:
		if prey[1] != 0:
			temp1 = prey[1] % prey[1]
		else:
			temp1 = prey[1]
	temp0 = max(prey[0], temp0)
	temp0 = temp0 - temp1
	if prey[1] != 0:
		temp2 = prey[0] / prey[1]
	else:
		temp2 = prey[1]
	temp0 = prey[0] - prey[0]
	temp1 = min(temp1, temp0)
	temp0 = min(prey[1], prey[0])
	temp3 = min(prey[0], temp0)
	temp0 = min(prey[0], temp2)
	temp0 = prey[1] + temp1
	if prey[0] > temp1:
		temp2 = prey[0] + temp0
	else:
		temp2 = -1 * prey[1]
	if temp2 != 0:
		temp2 = prey[0] / temp2
	else:
		temp2 = temp2
	return [temp1, temp1]