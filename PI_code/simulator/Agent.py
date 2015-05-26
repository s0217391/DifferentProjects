#!/usr/bin/python
import numpy as np
import abc
import random as r
import imp

class Agent:
	'Class representing an agent'
	ID_base = 0
	
	def __init__(self, behav, maxVelocity = 2.0, drag = 0.5,startPos = np.array([0.0, 0.0]), startVel = np.array([0.0, 0.0]), timestep = 1.0/25.0, energ = 25):
		Agent.ID_base += 1
		self.ID = Agent.ID_base
		self.pos = startPos
		self.vel = startVel
		self.mass = 1.0
		self.behavior = behav
		self.timestep = timestep
		self.maxVel = maxVelocity
		self.dragCoef = drag
		self.energy = energ
		self.distanceTravelled = 0
		
	def updateAgent(self, agents):
		force = 10 * self.behavior.compute(self, agents)
		if self.energy <= 0: force *= 0
		drag = -1.0 * self.dragCoef * self.vel
		force = force + drag
		self.vel = self.vel + self.timestep * (force / self.mass)
		velMag = np.sqrt(np.dot(self.vel, self.vel))
		if(velMag > self.maxVel):
			nrmlzd = self.vel / velMag
			self.vel = nrmlzd * self.maxVel
		self.pos = self.pos + self.timestep * self.vel

class Behaviour:
	'Class representing an agents behaviour'
	
	@abc.abstractmethod
	def compute(self, aself, agents):
		print 'abstract base class'
		
class runAwayBehaviour(Behaviour):
	'Prey Behaviour. Always runs away from everything within radius. Trapped when something else is close enough'
	
	def __init__(self, distanceDanger = 5.0, distanceTrapped = 1.0):
		self.thresDanger = distanceDanger
		self.thresTrapped = distanceTrapped
	
	def compute(self, aself, agents):
		trapped = False
		awayDirection = np.array([0.0, 0.0])
		for a in agents:
			if aself.ID == a.ID: 
				continue
			distToA = np.linalg.norm(aself.pos - a.pos)
			if(distToA < self.thresTrapped): 
				trapped = True
			elif distToA < self.thresDanger:
				awayDirection += (aself.pos - a.pos)
				aself.energy = max(0, aself.energy - 1)
		dirnorm = np.sqrt(np.dot(awayDirection, awayDirection))
		if trapped: 
			return np.array([0, 0])
		elif dirnorm > 0.01:
			direct = awayDirection
			nrml = awayDirection / dirnorm
			return nrml
		else:
			return np.array([0, 0])
			
class randomBehaviour(Behaviour):
	def compute(self, aself, agents):
		res = np.array([r.random(), r.random()])
		return res
		
class scriptedBehaviour(Behaviour):
	def __init__(self, module):
		self.scriptModule = imp.load_source("scriptedBehav", module)
		
	def compute(self, aself, agents):
		other = 1
		if aself.ID == agents[1].ID: 
			other = 2

		prey = agents[0]
		otherHunter = agents[other]

		relativePosPrey = prey.pos - aself.pos
		relativePosHunter = otherHunter.pos - aself.pos

		relatPreyOther = prey.pos - otherHunter.pos
		
		'distance between prey & other hunter'
		dist = np.linalg.norm(relatPreyOther)

		preyArr = [relativePosPrey[0], relativePosPrey[1]]
		otherHunterArr = [relativePosHunter[0], relativePosHunter[1]]
		force = self.scriptModule.compute(preyArr, otherHunterArr, dist)
		result = np.array(force)
		
		distToPrey = np.linalg.norm(relativePosPrey)
		if distToPrey < 3.5: 
			aself.energy = max(0, aself.energy - 1)

		return result
	
			
		
		

	
