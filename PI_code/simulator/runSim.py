#!/usr/bin/python
import sys
import numpy as np
import Agent as a 
import Simulator as s
import cv

def setup(dd, behavID, preyStart, hunter1Start, hunter2Start):
	sim = s.AgentSimulation()
	preyBehav = a.runAwayBehaviour(distanceTrapped = -1.0, distanceDanger = dd)
	basepath = "/home/i7674211/DifferentProjects/PI_code/simulator/behaviourGeneration/group/behav"
	huntBehav1 = a.scriptedBehaviour(basepath + str(behavID) + ".py")
	huntBehav2 = a.scriptedBehaviour(basepath + str(behavID) + ".py")

	prey = a.Agent(maxVelocity = 2.0, startPos = preyStart, drag = 0.1, behav = preyBehav)
	hunter1 = a.Agent(behav = huntBehav1, startPos = hunter1Start)
	hunter2 = a.Agent(behav = huntBehav2, startPos = hunter2Start)	

	sim.addAgent(prey)
	sim.addAgent(hunter1)
	sim.addAgent(hunter2)
	return sim

def convertPosition(pos):
	x = pos[0]
	y = pos[1]
	x = int(15 * x + 250)
	y = int(15 * y + 250)
	return (x, y)
	

def drawPositions(dd, sim, saveImage = False, filename = ''):
	positions = sim.getPositions()

	blank = cv.CreateMat(500, 500, cv.CV_8UC3)
	cv.AddS(blank, (255, 255, 255), blank)
	
	preyColor = (255, 0, 0)
	if sim.agents[0].energy <= 0: preyColor = (0, 255, 0)	
	
	cv.Circle(blank, convertPosition(positions[0]), 5, preyColor, thickness = -1)
	cv.Circle(blank, convertPosition(positions[0]), int(15.0 * dd), preyColor, thickness = 1)
	for i in (1, len(positions) - 1):
		hunterColor = (0, 0, 255)
		if sim.agents[i].energy <= 0: hunterColor = (0, 255, 0)
		cv.Circle(blank, convertPosition(positions[i]), 5, hunterColor, thickness = -1)
	cv.ShowImage("sim", blank)
	if saveImage:
		cv.SaveImage(filename, blank)
	cv.WaitKey(40)

preyPos = [[ 9,  3], [-6, -6], [5,  5], [-7, -6]]
huntPos1 = [[-8, -2], [ 6,  6], [5, -5], [ 7, -6]]
huntPos2 = [[-2, -8], [ 6,  -6], [-5, 5], [ -7, 6]]
"""
def main(argv=None):
	dd = 2
	f = open("result", 'w')
	for j in range(1, 501):
		f.write(str(j))
		for test in range(len(preyPos)):
			sim = setup(dd, behavID = j, preyStart = np.array(preyPos[test]), hunter1Start = np.array(huntPos1[test]), hunter2Start = np.array(huntPos2[test]))
			'startDistance = np.linalg.norm(np.array(preyPos[test]) - np.array(huntPos[test]))'
			steps = 200
			'averageDistance = 0'
			pos = 0
			for i in range(steps):
				sim.update()
				'averageDistance += np.linalg.norm(pos[0] - pos[1])'
				#drawPositions(dd, sim)
			'averageDistance = averageDistance / (steps * startDistance)'
			energyLevel = float(sim.agents[0].energy + 1) / float(sim.agents[1].energy + sim.agents[2].energy + 1)
			energyLevel *= min(np.linalg.norm(pos[0] - pos[1]), np.linalg.norm(pos[0] - pos[2]))
			f.write(" : " + str(energyLevel))
		f.write('\n')
"""
def main(argv=None):
	dd = 3.5
	for test in range(len(preyPos)):
		sim = setup(dd, behavID = 195, preyStart = np.array(preyPos[test]), hunter1Start = np.array(huntPos1[test]), hunter2Start = np.array(huntPos2[test]))
		steps = 300
		for i in range(steps):
				sim.update()
				drawPositions(dd, sim, saveImage = True, filename='outpic/frame' + str(test) + "_" + str(i) + ".png")

if __name__ == "__main__":
	sys.exit(main())
