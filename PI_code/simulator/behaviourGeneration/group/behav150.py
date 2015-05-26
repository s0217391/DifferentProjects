#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = otherHunter[0] * prey[0]
	temp1 = min( dist , prey[0] )
	temp1 = otherHunter[0] - otherHunter[1]
	temp1 = prey[1] - otherHunter[0]
	return [ otherHunter[0] , dist ]
