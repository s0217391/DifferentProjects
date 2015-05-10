#!/usr/bin/python
import Agent

class AgentSimulation:
	
	def __init__(self):
		self.agents = []
		
	def addAgent(self, agent):
		self.agents.append(agent)
		
	def update(self):
		for a in self.agents:
			a.updateAgent(self.agents)
			
	def getPositions(self):
		result = []
		for a in self.agents:
			result.append(a.pos)
		return result
		
