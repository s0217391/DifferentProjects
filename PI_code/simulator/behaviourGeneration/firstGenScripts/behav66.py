#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[0]
	temp1 = min(temp0, prey[1])
	if prey[0] != 0:
		temp0 = temp0 / prey[0]
	else:
		temp0 = prey[0]
	if prey[0] > temp0:
		temp2 = min(temp1, prey[1])
	else:
		temp2 = max(temp1, prey[1])
	if prey[0] != 0:
		temp3 = prey[1] % prey[0]
	else:
		temp3 = prey[0]
	temp4 = temp0 + prey[0]
	temp0 = -1 * temp4
	temp1 = temp2 * prey[1]
	temp3 = temp4 + prey[1]
	temp5 = temp2 - temp3
	temp4 = -1 * temp5
	if prey[1] != 0:
		temp6 = temp1 / prey[1]
	else:
		temp6 = prey[1]
	return [temp0, temp2]
