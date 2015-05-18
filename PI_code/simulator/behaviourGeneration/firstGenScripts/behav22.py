#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	if prey[1] > prey[0]:
		temp1 = min(prey[0], prey[0])
	else:
		temp1 = temp0 * temp0
	temp1 = temp1 + prey[1]
	temp1 = prey[1] - prey[0]
	temp1 = min(prey[0], temp1)
	if temp1 > temp1:
		if temp0 != 0:
			temp0 = prey[1] % temp0
		else:
			temp0 = temp0
	else:
		if temp1 > prey[1]:
			temp0 = min(prey[1], prey[1])
		else:
			temp0 = prey[1] + temp0
	return [temp0, prey[0]]
