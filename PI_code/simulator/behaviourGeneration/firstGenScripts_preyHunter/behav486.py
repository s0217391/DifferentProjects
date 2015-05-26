#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	if prey[1] > prey[1]:
		if prey[1] > prey[0]:
			temp1 = prey[1] + prey[1]
		else:
			if prey[1] != 0:
				temp1 = prey[1] % prey[1]
			else:
				temp1 = prey[1]
	else:
		if prey[0] > temp0:
			temp1 = temp0 - prey[1]
		else:
			temp1 = -1 * prey[0]
	temp0 = max(temp0, prey[0])
	temp2 = -1 * temp1
	if prey[1] > prey[0]:
		if temp1 > temp0:
			temp0 = min(temp1, prey[0])
		else:
			if prey[1] != 0:
				temp0 = prey[1] % prey[1]
			else:
				temp0 = prey[1]
	else:
		temp0 = temp0 - temp1
	if prey[0] != 0:
		temp3 = temp0 % prey[0]
	else:
		temp3 = prey[0]
	return [temp0, prey[1]]
