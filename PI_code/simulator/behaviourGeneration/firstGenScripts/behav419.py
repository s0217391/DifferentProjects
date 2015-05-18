#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[1]
	temp1 = prey[0] + temp0
	if prey[0] != 0:
		temp2 = temp1 / prey[0]
	else:
		temp2 = prey[0]
	temp3 = prey[0] + prey[0]
	temp3 = -1 * prey[1]
	if temp3 != 0:
		temp0 = prey[0] % temp3
	else:
		temp0 = temp3
	temp1 = -1 * temp3
	if prey[1] != 0:
		temp3 = prey[1] % prey[1]
	else:
		temp3 = prey[1]
	temp4 = temp1 - prey[1]
	temp0 = min(temp0, temp3)
	return [temp3, prey[1]]
