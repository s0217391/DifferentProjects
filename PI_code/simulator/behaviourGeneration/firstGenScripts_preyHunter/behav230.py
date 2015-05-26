#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] * prey[1]
	if prey[1] != 0:
		temp1 = prey[1] / prey[1]
	else:
		temp1 = prey[1]
	temp2 = -1 * temp1
	temp2 = temp1 * temp2
	if prey[1] != 0:
		temp3 = prey[1] / prey[1]
	else:
		temp3 = prey[1]
	temp4 = min(temp0, temp1)
	temp2 = -1 * temp4
	temp5 = min(prey[0], temp0)
	if temp3 > prey[0]:
		temp6 = min(temp1, temp2)
	else:
		temp6 = -1 * temp2
	temp7 = -1 * temp2
	temp8 = temp0 + temp4
	temp8 = -1 * temp2
	temp1 = temp1 - temp0
	temp6 = min(temp7, prey[0])
	temp2 = temp5 - temp7
	return [temp7, temp7]
