#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = -1 * temp0
	if prey[0] != 0:
		temp2 = prey[1] % prey[0]
	else:
		temp2 = prey[0]
	temp0 = prey[0] - prey[1]
	temp1 = temp2 * prey[1]
	temp3 = temp1 + prey[1]
	if temp1 > temp3:
		temp0 = prey[0] + prey[1]
	else:
		temp0 = -1 * temp3
	return [temp1, temp3]
