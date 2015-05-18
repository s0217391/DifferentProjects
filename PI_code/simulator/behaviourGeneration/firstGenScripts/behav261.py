#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	if prey[0] != 0:
		temp1 = prey[0] % prey[0]
	else:
		temp1 = prey[0]
	temp2 = temp1 + prey[0]
	temp1 = max(temp1, temp2)
	temp3 = min(temp1, prey[1])
	if prey[1] != 0:
		temp3 = temp2 / prey[1]
	else:
		temp3 = prey[1]
	temp4 = temp0 * temp2
	return [temp2, temp4]
