#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[0]
	if prey[1] != 0:
		temp1 = prey[0] / prey[1]
	else:
		temp1 = prey[1]
	temp1 = prey[0] + prey[0]
	temp1 = -1 * prey[1]
	temp1 = temp0 - temp1
	temp0 = min(temp0, prey[0])
	temp1 = max(temp0, temp0)
	temp1 = min(prey[1], prey[1])
	temp1 = max(prey[0], prey[0])
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	if temp0 != 0:
		temp1 = prey[1] % temp0
	else:
		temp1 = temp0
	temp0 = prey[0] * prey[0]
	temp0 = prey[0] - prey[1]
	temp2 = prey[1] - temp1
	temp1 = max(temp1, prey[1])
	if temp2 != 0:
		temp0 = prey[1] / temp2
	else:
		temp0 = temp2
	if temp2 > temp1:
		temp3 = max(temp2, prey[0])
	else:
		if temp1 > prey[1]:
			temp3 = min(prey[1], temp1)
		else:
			if temp1 > temp0:
				temp3 = temp1 - prey[1]
			else:
				if temp1 > prey[1]:
					if temp0 > temp0:
						temp3 = temp2 * temp2
					else:
						temp3 = min(prey[1], temp0)
				else:
					temp3 = prey[0] + temp2
	return [temp3, prey[1]]