#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	temp1 = prey[1] + prey[1]
	temp2 = prey[0] - temp1
	if prey[0] != 0:
		temp3 = temp2 / prey[0]
	else:
		temp3 = prey[0]
	temp1 = min(prey[0], temp3)
	temp2 = temp3 * temp0
	if temp0 != 0:
		temp2 = temp2 / temp0
	else:
		temp2 = temp0
	if temp2 != 0:
		temp0 = temp2 % temp2
	else:
		temp0 = temp2
	if prey[0] != 0:
		temp4 = temp3 / prey[0]
	else:
		temp4 = prey[0]
	temp5 = min(temp3, temp1)
	temp3 = -1 * temp0
	temp5 = -1 * prey[1]
	if temp3 > temp4:
		if temp0 != 0:
			temp2 = prey[1] % temp0
		else:
			temp2 = temp0
	else:
		temp2 = temp4 - temp2
	if prey[1] != 0:
		temp4 = prey[1] % prey[1]
	else:
		temp4 = prey[1]
	temp3 = temp3 + temp4
	temp1 = temp4 - temp3
	temp5 = -1 * temp1
	temp6 = temp1 - temp5
	temp2 = min(prey[1], prey[1])
	if temp0 != 0:
		temp5 = temp4 / temp0
	else:
		temp5 = temp0
	return [temp0, temp4]
