#!/usr/bin/python
import sys

def compute(prey, otherHunter, dist):
	temp0 = max( prey[0] , dist )
	temp1 = dist + temp0
	temp1 = prey[1] + otherHunter[1]
	return [ otherHunter[0] , otherHunter[0] ]
