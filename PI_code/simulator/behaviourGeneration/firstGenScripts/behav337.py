#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] % prey[0]
	else:
		temp0 = prey[0]
	if temp0 > prey[1]:
		if prey[1] != 0:
			temp1 = prey[0] % prey[1]
		else:
			temp1 = prey[1]
	else:
		if prey[1] > prey[1]:
			if temp0 != 0:
				temp1 = prey[1] / temp0
			else:
				temp1 = temp0
		else:
			temp1 = max(prey[1], temp0)
	if prey[1] > temp0:
		if prey[1] != 0:
			temp0 = prey[0] % prey[1]
		else:
			temp0 = prey[1]
	else:
		temp0 = min(temp1, prey[1])
	return [temp0, prey[1]]
