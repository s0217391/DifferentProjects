#ifndef SANDPILE_H
#define SANDPILE_H

#include "force.h"
#include "integrator.h"
#include "particle.h"

class Sand{

public:
  inline Sand() {;}

  inline addParticle(Particle _p) {m_particles.push_back(_p);}
  inline clearParticles() {m_particles.clear();}


  inline addForce(ForcePtr _f) {m_forces.push_back(_f);}
  inline clearForces() {m_forces.clear();}

  void updateParticles();

  void getPositions(std::vector<ngl::Vec3> & o_positions);

private:
  ParticleVector m_particles;
  // Pointers because abstract class. Using smart pointers to avoid memory leaks.
  IntegratorSPtr m_integrator;
  ForcePtrVec m_forces;


};

#endif // SANDPILE_H
