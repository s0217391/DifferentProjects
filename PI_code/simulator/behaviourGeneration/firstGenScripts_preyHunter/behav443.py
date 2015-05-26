#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[0])
	if temp0 != 0:
		temp1 = prey[0] % temp0
	else:
		temp1 = temp0
	temp2 = temp0 * temp1
	temp3 = -1 * temp0
	temp0 = temp2 + temp0
	if prey[0] > temp0:
		temp3 = prey[1] * temp0
	else:
		if temp0 > temp3:
			if temp0 > temp2:
				temp3 = -1 * temp2
			else:
				if temp0 != 0:
					temp3 = temp0 % temp0
				else:
					temp3 = temp0
		else:
			if temp0 != 0:
				temp3 = temp1 / temp0
			else:
				temp3 = temp0
	temp3 = prey[1] * temp1
	temp2 = temp2 * temp0
	if temp2 > temp0:
		temp3 = temp0 - temp2
	else:
		temp3 = min(temp2, temp0)
	temp4 = min(temp2, temp2)
	temp3 = -1 * temp2
	return [temp4, prey[0]]
