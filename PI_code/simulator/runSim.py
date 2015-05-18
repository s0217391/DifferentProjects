#!/usr/bin/python
import sys
import numpy as np
import Agent as a 
import Simulator as s
import cv

def setup(dd, behavID, preyStart, hunterStart):
	sim = s.AgentSimulation()
	preyBehav = a.runAwayBehaviour(distanceTrapped = -1.0, distanceDanger = dd)
	basepath = "/home/i7674211/DifferentProjects/PI_code/simulator/behaviourGeneration/firstGenScripts/behav"
	rndmBehav = a.scriptedBehaviour(basepath + str(behavID) + ".py")
	prey = a.Agent(maxVelocity = 1.0, startPos = preyStart, drag = 1, behav = preyBehav)
	hunter = a.Agent(behav = rndmBehav, startPos = hunterStart)
	sim.addAgent(prey)
	sim.addAgent(hunter)
	return sim

def convertPosition(pos):
	x = pos[0]
	y = pos[1]
	x = int(25 * x + 250)
	y = int(25 * y + 250)
	return (x, y)
	

def drawPositions(dd, positions = [], saveImage = False, filename = ''):
	blank = cv.CreateMat(500, 500, cv.CV_8UC3)
	cv.AddS(blank, (255, 255, 255), blank)
	cv.Circle(blank, convertPosition(positions[0]), 5, (255, 0, 0), thickness = -1)
	cv.Circle(blank, convertPosition(positions[0]), int(25.0 * dd), (255, 0, 0), thickness = 1)
	for i in positions[1:]:
		cv.Circle(blank, convertPosition(i), 5, (0, 0, 255), thickness = -1)
	cv.ShowImage("sim", blank)
	if saveImage:
		cv.SaveImage(filename, blank)
	cv.WaitKey(40)

preyPos = [[ 9,  3], [-6, -6], [5,  5], [-7, -6]]
huntPos = [[-8, -2], [ 6,  6], [5, -5], [ 7, -6]]

"""
def main(argv=None):
	dd = 2
	f = open("result", 'w')
	for j in range(1, 501):
		f.write(str(j))
		for test in range(len(preyPos)):
			sim = setup(dd, behavID = j, preyStart = np.array(preyPos[test]), hunterStart = np.array(huntPos[test]))
			startDistance = np.linalg.norm(np.array(preyPos[test]) - np.array(huntPos[test]))
			steps = 200
			averageDistance = 0
			for i in range(steps):
				sim.update()
				pos = sim.getPositions()
				averageDistance += np.linalg.norm(pos[0] - pos[1])
				#drawPositions(dd, pos)
			averageDistance = averageDistance / (steps * startDistance)
			f.write(" : " + str(averageDistance))
		f.write('\n')
"""
def main(argv=None):
	dd = 2
	for test in range(len(preyPos)):
		sim = setup(dd, behavID = 41, preyStart = np.array(preyPos[test]), hunterStart = np.array(huntPos[test]))
		steps = 200
		for i in range(steps):
				sim.update()
				pos = sim.getPositions()
				drawPositions(dd, pos, saveImage = True, filename='outpic/frame' + str(test) + "_" + str(i) + ".png")
			
if __name__ == "__main__":
	sys.exit(main())
