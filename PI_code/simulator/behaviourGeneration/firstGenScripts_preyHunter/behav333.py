#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[1], prey[0])
	if prey[1] != 0:
		temp1 = prey[0] % prey[1]
	else:
		temp1 = prey[1]
	if prey[1] > temp1:
		temp2 = -1 * prey[1]
	else:
		temp2 = -1 * prey[0]
	if temp1 != 0:
		temp1 = temp1 / temp1
	else:
		temp1 = temp1
	temp2 = temp1 * temp2
	if temp1 != 0:
		temp3 = temp0 % temp1
	else:
		temp3 = temp1
	temp3 = temp3 + prey[0]
	if prey[1] > prey[0]:
		temp3 = prey[1] * temp0
	else:
		temp3 = prey[0] + temp0
	return [temp3, temp0]
