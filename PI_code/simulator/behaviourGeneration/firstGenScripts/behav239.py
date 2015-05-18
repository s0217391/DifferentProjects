#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] + prey[0]
	temp1 = prey[0] - prey[1]
	temp0 = prey[0] + temp1
	temp2 = min(temp1, temp0)
	if temp2 > prey[0]:
		temp2 = min(prey[1], prey[1])
	else:
		if temp2 > temp2:
			temp2 = temp1 - prey[0]
		else:
			temp2 = prey[0] + prey[1]
	temp3 = min(temp2, prey[1])
	temp3 = min(prey[1], prey[1])
	temp4 = min(prey[1], temp3)
	temp1 = -1 * temp4
	temp5 = prey[1] - temp3
	temp0 = min(temp4, temp1)
	if temp1 != 0:
		temp5 = temp4 / temp1
	else:
		temp5 = temp1
	if prey[1] > temp5:
		if temp0 > temp0:
			temp6 = temp4 - temp1
		else:
			temp6 = temp1 - temp3
	else:
		temp6 = -1 * temp1
	temp0 = min(temp2, temp5)
	temp4 = -1 * temp1
	if temp6 != 0:
		temp6 = prey[0] % temp6
	else:
		temp6 = temp6
	temp1 = min(temp6, prey[1])
	if temp2 != 0:
		temp6 = temp5 % temp2
	else:
		temp6 = temp2
	temp6 = min(prey[0], temp2)
	temp0 = temp3 * temp6
	if prey[0] != 0:
		temp6 = temp1 % prey[0]
	else:
		temp6 = prey[0]
	return [temp2, temp2]
