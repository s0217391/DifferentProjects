#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] > prey[0]:
		if prey[1] != 0:
			temp0 = prey[1] / prey[1]
		else:
			temp0 = prey[1]
	else:
		temp0 = min(prey[1], prey[1])
	if prey[1] != 0:
		temp1 = temp0 % prey[1]
	else:
		temp1 = prey[1]
	if prey[1] != 0:
		temp1 = temp0 / prey[1]
	else:
		temp1 = prey[1]
	temp2 = max(temp1, temp1)
	if prey[0] != 0:
		temp0 = prey[0] / prey[0]
	else:
		temp0 = prey[0]
	temp2 = -1 * temp1
	temp2 = min(temp0, temp1)
	temp3 = max(temp2, prey[0])
	if temp0 != 0:
		temp2 = temp0 / temp0
	else:
		temp2 = temp0
	if temp3 != 0:
		temp3 = prey[1] / temp3
	else:
		temp3 = temp3
	temp0 = temp2 + prey[1]
	temp4 = temp3 + temp3
	return [temp4, temp3]
