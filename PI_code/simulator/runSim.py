#!/usr/bin/python
import sys
import numpy as np
import Agent as a 
import Simulator as s
import cv

def setup(dd):
	sim = s.AgentSimulation()
	preyBehav = a.runAwayBehaviour(distanceTrapped = -1.0, distanceDanger = dd)
	rndmBehav = a.scriptedBehaviour("/home/i7674211/DifferentProjects/PI_code/simulator/behaviourGeneration/generatedBehaviour.py")
	prey = a.Agent(maxVelocity = 1.0, drag = 1, behav = preyBehav)
	hunter = a.Agent(behav = rndmBehav, startPos = np.array([-3, -3]))
	sim.addAgent(prey)
	sim.addAgent(hunter)
	return sim

def convertPosition(pos):
	x = pos[0]
	y = pos[1]
	x = 25 * x + 250
	y = 25 * y + 250
	return (x, y)
	

def drawPositions(dd, positions = []):
	blank = cv.CreateMat(500, 500, cv.CV_8UC3)
	cv.AddS(blank, (255, 255, 255), blank)
	cv.Circle(blank, convertPosition(positions[0]), 5, (255, 0, 0), thickness = -1)
	cv.Circle(blank, convertPosition(positions[0]), 25.0 * dd, (255, 0, 0), thickness = 1)
	for i in positions[1:]:
		cv.Circle(blank, convertPosition(i), 5, (0, 0, 255), thickness = -1)
	cv.ShowImage("sim", blank)
	cv.WaitKey(40)

def main(argv=None):
	dd = 2
	sim = setup(dd)
	steps = 200
	for i in range(steps):
		sim.update()
		pos = sim.getPositions()
		print pos
		drawPositions(dd, pos)
	
if __name__ == "__main__":
	sys.exit(main())
