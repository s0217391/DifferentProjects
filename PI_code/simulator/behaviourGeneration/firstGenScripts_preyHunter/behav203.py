#!/usr/bin/python
import sys

def compute(prey):
	if prey[0] != 0:
		temp0 = prey[1] / prey[0]
	else:
		temp0 = prey[0]
	temp1 = min(prey[0], prey[0])
	if temp0 != 0:
		temp1 = prey[1] / temp0
	else:
		temp1 = temp0
	temp0 = max(temp0, prey[0])
	temp0 = max(prey[1], temp1)
	if prey[1] != 0:
		temp2 = temp1 % prey[1]
	else:
		temp2 = prey[1]
	temp0 = temp2 - temp1
	if prey[1] != 0:
		temp1 = temp2 / prey[1]
	else:
		temp1 = prey[1]
	temp0 = min(prey[0], temp0)
	temp2 = min(temp0, prey[1])
	if temp2 != 0:
		temp3 = prey[1] / temp2
	else:
		temp3 = temp2
	temp4 = temp2 + prey[1]
	temp5 = prey[1] * temp4
	temp3 = temp3 - prey[0]
	if prey[0] != 0:
		temp3 = prey[1] / prey[0]
	else:
		temp3 = prey[0]
	temp0 = prey[0] + temp5
	if prey[1] != 0:
		temp1 = prey[0] % prey[1]
	else:
		temp1 = prey[1]
	if temp4 != 0:
		temp3 = temp3 % temp4
	else:
		temp3 = temp4
	if temp1 != 0:
		temp3 = prey[1] / temp1
	else:
		temp3 = temp1
	temp3 = temp2 + temp5
	return [temp3, temp1]
