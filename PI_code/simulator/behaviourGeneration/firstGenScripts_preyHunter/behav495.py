#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	if prey[0] != 0:
		temp1 = temp0 / prey[0]
	else:
		temp1 = prey[0]
	temp0 = min(temp0, prey[1])
	temp1 = min(prey[0], temp1)
	if temp1 != 0:
		temp2 = prey[1] % temp1
	else:
		temp2 = temp1
	if prey[1] > temp1:
		temp1 = min(temp0, temp0)
	else:
		if prey[0] != 0:
			temp1 = temp1 / prey[0]
		else:
			temp1 = prey[0]
	temp0 = temp0 * prey[0]
	temp0 = -1 * temp0
	if prey[0] != 0:
		temp1 = temp2 % prey[0]
	else:
		temp1 = prey[0]
	temp1 = max(temp0, temp1)
	temp3 = -1 * temp2
	temp2 = temp1 + temp2
	temp2 = temp3 * temp1
	temp3 = temp0 * temp1
	temp2 = max(temp2, temp1)
	temp3 = -1 * temp1
	temp3 = temp3 * temp2
	return [temp1, prey[1]]