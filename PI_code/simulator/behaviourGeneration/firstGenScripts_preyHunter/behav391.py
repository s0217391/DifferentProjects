#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[1]
	temp1 = temp0 + prey[1]
	temp0 = prey[1] + prey[1]
	temp0 = prey[0] - temp0
	if temp0 > prey[0]:
		if temp1 != 0:
			temp2 = temp0 / temp1
		else:
			temp2 = temp1
	else:
		temp2 = prey[1] + temp1
	if prey[0] != 0:
		temp2 = temp2 / prey[0]
	else:
		temp2 = prey[0]
	temp3 = min(prey[1], temp0)
	temp1 = min(temp2, temp3)
	temp1 = min(temp2, temp2)
	if temp0 > temp2:
		if prey[1] > temp3:
			temp0 = -1 * temp3
		else:
			temp0 = min(prey[0], prey[1])
	else:
		temp0 = min(temp0, temp0)
	temp0 = prey[1] - prey[0]
	temp1 = temp2 + temp0
	temp1 = prey[1] + temp3
	temp4 = max(temp0, prey[0])
	temp2 = temp0 * temp2
	if temp3 > temp0:
		temp4 = min(temp1, prey[0])
	else:
		temp4 = min(prey[0], temp3)
	return [temp1, temp4]