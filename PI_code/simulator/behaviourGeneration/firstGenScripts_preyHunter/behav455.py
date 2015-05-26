#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	if temp0 != 0:
		temp1 = prey[0] / temp0
	else:
		temp1 = temp0
	temp0 = -1 * temp1
	if prey[0] > prey[1]:
		temp2 = temp1 * prey[0]
	else:
		temp2 = min(temp0, prey[0])
	if prey[1] != 0:
		temp3 = temp2 % prey[1]
	else:
		temp3 = prey[1]
	temp2 = temp0 - temp1
	temp1 = temp2 + prey[1]
	temp1 = temp2 - temp1
	if prey[0] > temp1:
		if temp1 > temp0:
			temp0 = temp0 + prey[0]
		else:
			if temp3 != 0:
				temp0 = prey[1] % temp3
			else:
				temp0 = temp3
	else:
		temp0 = max(temp0, prey[0])
	return [temp0, prey[1]]
