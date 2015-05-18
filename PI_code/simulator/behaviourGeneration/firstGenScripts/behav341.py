#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[1]
	temp1 = prey[0] * temp0
	if temp0 > prey[0]:
		temp2 = max(prey[1], prey[1])
	else:
		temp2 = temp0 - temp0
	temp0 = prey[1] + temp1
	temp0 = max(temp0, temp2)
	temp3 = min(prey[0], temp2)
	temp4 = -1 * temp0
	if temp2 > temp3:
		temp5 = min(prey[0], temp0)
	else:
		temp5 = min(temp4, temp4)
	temp1 = prey[0] * temp4
	temp6 = min(temp1, prey[1])
	temp2 = prey[1] * temp6
	if prey[0] != 0:
		temp1 = temp3 / prey[0]
	else:
		temp1 = prey[0]
	return [temp6, temp2]
