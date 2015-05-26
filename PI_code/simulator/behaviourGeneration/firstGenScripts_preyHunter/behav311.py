#!/usr/bin/python
import sys

def compute(prey):
	temp0 = prey[1] - prey[0]
	temp1 = max(prey[0], temp0)
	temp2 = temp0 - prey[0]
	if temp2 != 0:
		temp0 = temp0 % temp2
	else:
		temp0 = temp2
	if prey[1] != 0:
		temp1 = prey[0] % prey[1]
	else:
		temp1 = prey[1]
	temp0 = temp1 + temp2
	temp2 = min(prey[1], temp0)
	temp1 = max(temp0, temp2)
	temp2 = temp0 - temp0
	if temp2 > temp1:
		if prey[0] != 0:
			temp0 = temp0 / prey[0]
		else:
			temp0 = prey[0]
	else:
		temp0 = max(temp1, temp1)
	if prey[1] != 0:
		temp3 = temp0 % prey[1]
	else:
		temp3 = prey[1]
	temp0 = prey[1] - temp2
	temp2 = max(prey[0], temp3)
	temp3 = prey[1] * temp2
	temp3 = min(prey[0], temp1)
	return [temp1, temp1]
