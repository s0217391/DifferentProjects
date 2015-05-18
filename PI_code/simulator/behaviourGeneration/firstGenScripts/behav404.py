#!/usr/bin/python
import sys

def compute(prey):
	temp0 = min(prey[1], prey[1])
	temp1 = max(temp0, temp0)
	temp2 = min(temp1, temp1)
	temp3 = temp0 - temp1
	if temp2 != 0:
		temp3 = temp3 % temp2
	else:
		temp3 = temp2
	temp3 = prey[1] + temp2
	temp1 = min(temp1, prey[0])
	if temp3 > temp1:
		if temp2 != 0:
			temp2 = temp2 % temp2
		else:
			temp2 = temp2
	else:
		temp2 = temp3 + prey[0]
	return [temp2, temp2]
