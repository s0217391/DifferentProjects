#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[0]
	temp1 = prey[0] * prey[1]
	if temp0 > prey[0]:
		temp0 = min(prey[0], prey[1])
	else:
		if prey[1] != 0:
			temp0 = temp0 / prey[1]
		else:
			temp0 = prey[1]
	temp1 = -1 * prey[0]
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	if prey[1] > temp1:
		if temp1 != 0:
			temp2 = temp1 / temp1
		else:
			temp2 = temp1
	else:
		if prey[0] != 0:
			temp2 = prey[0] % prey[0]
		else:
			temp2 = prey[0]
	if prey[0] != 0:
		temp3 = prey[0] / prey[0]
	else:
		temp3 = prey[0]
	if temp3 > temp3:
		temp3 = prey[1] * prey[0]
	else:
		temp3 = temp0 + temp3
	temp2 = prey[1] - prey[1]
	temp0 = temp0 * temp3
	temp2 = temp0 + prey[0]
	return [temp0, prey[1]]
