#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[0] + prey[0]
	temp1 = max(temp0, prey[0])
	temp2 = temp1 + prey[1]
	temp0 = prey[0] + prey[0]
	temp1 = temp0 * temp2
	if temp2 != 0:
		temp3 = prey[1] % temp2
	else:
		temp3 = temp2
	if temp2 != 0:
		temp2 = temp0 / temp2
	else:
		temp2 = temp2
	temp3 = temp3 - temp2
	temp4 = max(prey[0], prey[1])
	temp4 = -1 * temp4
	if temp4 > temp3:
		temp3 = temp3 * temp3
	else:
		temp3 = temp1 * temp3
	if temp2 != 0:
		temp3 = prey[0] % temp2
	else:
		temp3 = temp2
	temp5 = prey[1] * temp0
	temp2 = temp0 - temp0
	if prey[0] > prey[0]:
		temp2 = temp5 * temp4
	else:
		temp2 = temp3 * prey[1]
	temp0 = temp2 + temp1
	if temp1 != 0:
		temp5 = prey[0] % temp1
	else:
		temp5 = temp1
	temp0 = min(temp3, temp0)
	temp1 = prey[0] - temp4
	temp1 = -1 * prey[1]
	if prey[1] != 0:
		temp2 = temp1 / prey[1]
	else:
		temp2 = prey[1]
	return [temp3, temp5]
