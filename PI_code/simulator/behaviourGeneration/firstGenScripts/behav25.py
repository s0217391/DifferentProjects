#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] > prey[1]:
		temp0 = prey[1] + prey[0]
	else:
		if prey[1] != 0:
			temp0 = prey[0] % prey[1]
		else:
			temp0 = prey[1]
	temp1 = max(temp0, prey[0])
	temp2 = prey[1] + temp1
	temp1 = max(temp2, prey[1])
	temp3 = temp2 + temp1
	if temp2 > prey[0]:
		temp4 = max(prey[0], temp2)
	else:
		temp4 = -1 * temp1
	if prey[1] != 0:
		temp5 = prey[1] % prey[1]
	else:
		temp5 = prey[1]
	if temp4 != 0:
		temp4 = temp1 / temp4
	else:
		temp4 = temp4
	temp5 = temp4 * temp2
	temp1 = min(temp1, temp1)
	temp5 = temp2 + temp3
	temp4 = min(prey[1], temp0)
	temp2 = -1 * temp3
	temp0 = temp3 * temp3
	temp6 = temp3 * temp4
	temp3 = temp5 + prey[0]
	temp4 = -1 * temp2
	temp1 = temp3 + prey[0]
	temp5 = prey[1] + temp5
	return [temp2, temp5]
