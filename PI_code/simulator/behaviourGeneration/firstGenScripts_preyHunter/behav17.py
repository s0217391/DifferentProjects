#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[1])
	temp1 = prey[1] * prey[0]
	if temp1 != 0:
		temp0 = prey[1] % temp1
	else:
		temp0 = temp1
	if prey[0] > temp0:
		temp2 = temp1 * prey[1]
	else:
		temp2 = min(temp0, prey[1])
	temp0 = -1 * temp1
	temp2 = prey[0] * prey[1]
	if temp2 != 0:
		temp2 = temp2 % temp2
	else:
		temp2 = temp2
	if temp1 > prey[0]:
		temp1 = temp0 - temp0
	else:
		if prey[1] != 0:
			temp1 = temp2 / prey[1]
		else:
			temp1 = prey[1]
	if prey[1] != 0:
		temp3 = prey[0] / prey[1]
	else:
		temp3 = prey[1]
	temp0 = temp2 + temp3
	if temp1 != 0:
		temp4 = prey[1] % temp1
	else:
		temp4 = temp1
	return [temp1, prey[0]]
