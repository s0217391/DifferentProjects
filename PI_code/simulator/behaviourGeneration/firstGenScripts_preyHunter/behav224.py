#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[1])
	if prey[1] != 0:
		temp1 = prey[1] % prey[1]
	else:
		temp1 = prey[1]
	if prey[0] != 0:
		temp2 = prey[1] / prey[0]
	else:
		temp2 = prey[0]
	temp1 = prey[1] + temp1
	if prey[1] > temp2:
		temp3 = prey[1] - temp0
	else:
		temp3 = max(prey[1], temp2)
	temp2 = temp1 - temp2
	temp4 = max(prey[0], prey[1])
	temp0 = temp4 - temp4
	temp0 = prey[1] - prey[1]
	temp4 = prey[0] * temp1
	return [temp2, prey[0]]