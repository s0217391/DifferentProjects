#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[0])
	temp1 = prey[1] - prey[0]
	if temp1 != 0:
		temp0 = temp1 / temp1
	else:
		temp0 = temp1
	if temp1 != 0:
		temp1 = prey[1] % temp1
	else:
		temp1 = temp1
	temp0 = prey[0] - temp1
	temp2 = prey[0] + temp1
	temp2 = temp2 - prey[1]
	temp3 = max(temp1, temp1)
	temp3 = -1 * temp3
	if prey[1] != 0:
		temp4 = temp0 / prey[1]
	else:
		temp4 = prey[1]
	temp0 = -1 * temp1
	temp0 = min(temp4, temp0)
	if prey[0] != 0:
		temp5 = prey[0] % prey[0]
	else:
		temp5 = prey[0]
	if temp5 != 0:
		temp0 = prey[0] % temp5
	else:
		temp0 = temp5
	temp2 = temp2 * temp1
	temp1 = prey[0] + temp3
	temp6 = max(temp0, temp0)
	if temp6 > temp6:
		temp0 = temp5 + prey[1]
	else:
		temp0 = max(temp3, temp6)
	temp1 = min(temp5, temp2)
	temp3 = min(temp4, temp1)
	temp5 = min(temp1, temp0)
	temp0 = min(prey[0], temp2)
	if temp3 != 0:
		temp1 = temp4 / temp3
	else:
		temp1 = temp3
	return [temp5, prey[0]]
