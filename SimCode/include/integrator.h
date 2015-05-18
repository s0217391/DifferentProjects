#ifndef INTEGRATOR_H
#define INTEGRATOR_H

// Based on code from earlier project.

#include "boost/scoped_ptr.hpp"

#include "particle.h"

class Integrator
{
public:
  virtual void updateSystem(ParticleVector & io_particles) const = 0;

  /*
   * timestep getter/setter
   */
  inline float getTimeStep() const {return m_timestep;}
  inline void setTimeStep(float _newStep) {m_timestep = _newStep;}

private:
  // timestep member
  float m_timestep;

protected:
  // Constructor for initializing the timestep.
  inline Integrator(float _timestep) : m_timestep(_timestep) {}
};

typedef boost::scoped_ptr<Integrator> IntegratorSPtr;

#endif // INTEGRATOR_H
