#!/usr/bin/python
import sys

def compute(prey):
	temp0 = -1 * prey[1]
	temp1 = prey[1] + temp0
	temp1 = prey[1] + temp1
	temp1 = temp0 - temp1
	if prey[0] != 0:
		temp2 = temp1 % prey[0]
	else:
		temp2 = prey[0]
	temp1 = temp0 * prey[1]
	if temp0 > temp0:
		temp1 = max(prey[0], temp0)
	else:
		temp1 = prey[0] - temp2
	if prey[1] != 0:
		temp0 = prey[0] % prey[1]
	else:
		temp0 = prey[1]
	temp3 = max(temp1, temp0)
	temp4 = max(temp1, prey[1])
	if prey[0] > temp2:
		temp2 = max(temp4, prey[0])
	else:
		temp2 = temp0 * temp2
	if prey[0] != 0:
		temp1 = temp4 / prey[0]
	else:
		temp1 = prey[0]
	temp5 = temp2 * prey[1]
	temp3 = max(prey[0], temp3)
	temp3 = -1 * temp2
	temp6 = max(prey[1], temp3)
	if temp3 > temp5:
		temp3 = temp5 + prey[0]
	else:
		temp3 = -1 * temp3
	return [temp1, temp6]
