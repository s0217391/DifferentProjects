#!/usr/bin/python
import sys

def compute(prey):
	if prey[1] != 0:
		temp0 = prey[1] / prey[1]
	else:
		temp0 = prey[1]
	temp1 = max(temp0, prey[0])
	temp1 = -1 * prey[1]
	temp1 = prey[1] - temp1
	temp2 = max(prey[0], prey[1])
	temp1 = -1 * temp0
	temp3 = min(temp1, temp0)
	if temp3 != 0:
		temp4 = prey[1] / temp3
	else:
		temp4 = temp3
	temp2 = temp1 - temp2
	if prey[0] != 0:
		temp2 = temp3 % prey[0]
	else:
		temp2 = prey[0]
	if temp2 != 0:
		temp5 = temp3 % temp2
	else:
		temp5 = temp2
	if temp2 != 0:
		temp1 = temp5 % temp2
	else:
		temp1 = temp2
	if prey[1] > temp1:
		temp5 = min(temp1, prey[0])
	else:
		temp5 = min(temp2, temp4)
	temp4 = temp2 - temp5
	return [temp2, prey[1]]
