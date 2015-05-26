#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[0])
	temp1 = temp0 - prey[0]
	temp2 = min(temp0, prey[0])
	if prey[0] != 0:
		temp3 = temp2 / prey[0]
	else:
		temp3 = prey[0]
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	temp4 = temp2 - prey[1]
	temp4 = min(temp2, temp2)
	if temp2 > prey[1]:
		temp1 = max(temp2, temp3)
	else:
		if prey[1] > prey[0]:
			if temp1 != 0:
				temp1 = temp0 % temp1
			else:
				temp1 = temp1
		else:
			temp1 = temp2 - temp0
	temp0 = min(temp2, prey[1])
	if temp0 > prey[1]:
		temp3 = prey[1] + temp2
	else:
		if prey[1] > prey[1]:
			temp3 = temp1 + temp4
		else:
			temp3 = max(temp0, temp1)
	temp5 = prey[0] + temp4
	if prey[0] != 0:
		temp3 = temp4 / prey[0]
	else:
		temp3 = prey[0]
	return [temp2, prey[1]]
