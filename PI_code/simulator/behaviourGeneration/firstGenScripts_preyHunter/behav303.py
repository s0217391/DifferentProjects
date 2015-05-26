#!/usr/bin/python
import sys

def compute(prey):
	temp0 = max(prey[0], prey[0])
	temp1 = min(temp0, temp0)
	if prey[0] != 0:
		temp0 = temp1 / prey[0]
	else:
		temp0 = prey[0]
	temp2 = max(temp1, temp1)
	if prey[1] != 0:
		temp1 = temp1 % prey[1]
	else:
		temp1 = prey[1]
	if prey[1] != 0:
		temp0 = prey[1] % prey[1]
	else:
		temp0 = prey[1]
	temp3 = min(prey[0], prey[0])
	temp2 = -1 * temp2
	temp0 = temp3 + temp3
	temp3 = temp0 * temp1
	temp2 = prey[0] * prey[0]
	temp4 = min(temp1, temp0)
	if temp0 != 0:
		temp2 = temp1 % temp0
	else:
		temp2 = temp0
	temp5 = max(temp1, temp0)
	temp3 = max(temp3, prey[1])
	temp6 = -1 * temp5
	temp3 = temp3 * temp4
	temp3 = temp6 + temp3
	temp6 = max(prey[0], temp2)
	if temp2 != 0:
		temp3 = temp4 / temp2
	else:
		temp3 = temp2
	temp7 = max(temp2, temp0)
	if prey[0] != 0:
		temp5 = temp1 % prey[0]
	else:
		temp5 = prey[0]
	temp8 = temp6 + temp3
	if temp6 != 0:
		temp8 = temp3 % temp6
	else:
		temp8 = temp6
	temp3 = temp0 - temp3
	return [temp6, temp5]
