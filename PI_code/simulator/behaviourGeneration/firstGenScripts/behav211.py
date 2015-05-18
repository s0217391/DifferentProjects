#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[0] % prey[0]
	else:
		temp0 = prey[0]
	temp1 = prey[1] * prey[0]
	temp2 = prey[0] - prey[0]
	if prey[1] != 0:
		temp3 = prey[1] / prey[1]
	else:
		temp3 = prey[1]
	if prey[1] > temp1:
		temp3 = max(prey[0], temp2)
	else:
		temp3 = temp2 * temp2
	temp3 = max(temp3, temp2)
	temp3 = max(temp1, prey[1])
	if prey[0] > temp1:
		temp3 = temp2 - prey[0]
	else:
		temp3 = -1 * temp1
	temp2 = -1 * prey[0]
	if temp1 != 0:
		temp2 = temp2 / temp1
	else:
		temp2 = temp1
	temp0 = prey[1] + prey[0]
	return [temp0, temp3]
