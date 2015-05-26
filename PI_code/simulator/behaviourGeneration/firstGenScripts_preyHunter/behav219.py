#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[0]
	temp1 = prey[0] + prey[1]
	if prey[1] != 0:
		temp0 = prey[0] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = temp0 - prey[0]
	temp1 = prey[0] * temp0
	temp2 = -1 * temp0
	temp3 = -1 * temp0
	temp3 = min(prey[1], prey[0])
	if prey[0] > prey[1]:
		if temp0 != 0:
			temp3 = temp1 % temp0
		else:
			temp3 = temp0
	else:
		temp3 = max(temp2, temp3)
	return [temp0, prey[0]]
