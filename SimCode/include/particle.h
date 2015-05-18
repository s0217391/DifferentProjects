#ifndef PARTICLE_H
#define PARTICLE_H

#include <vector>

#include "ngl/VAOPrimitives.h"

class Particle
{
public:
  inline Particle(float _rad, float _mass, ngl::Vec3 _pos, ngl::Vec3 _vel = ngl::Vec3(0, 0, 0)) :
                                              m_radius(_rad),
                                              m_mass(_mass),
                                              m_invMass(1.0f / _mass),
                                              m_position(_pos),
                                              m_velocity(_vel),
                                              m_forceAccumulator(ngl::Vec3()) {}

  inline float getRadius() {return m_radius;}


  inline float getMass() {return m_mass;}
  inline float getInvMass() {return m_invMass;}

  inline ngl::Vec3 getPosition() {return m_position;}
  inline void updatePosition(ngl::Vec3 _newPos) {m_position = _newPos;}

  inline ngl::Vec3 getVelocity() {return m_velocity;}
  inline void updateVelocity(ngl::Vec3 _newVel) {m_velocity = _newVel;}

  inline ngl::Vec3 getAcceleration() {return m_forceAccumulator * getInvMass();}
  inline ngl::Vec3 getForceAccumulator() {return m_forceAccumulator;}
  inline void exertForce(ngl::Vec3 _force) {m_forceAccumulator = _force;}


private:
  // Our particles will have to have a radius, as they collide with one another
  const float m_radius;
  // Mass of the particle
  const float m_mass;
  // Inverse mass of the particle. Stored so we have to compute it only once.
  const float m_invMass;

  // Members for position, velocity, force accumulator
  ngl::Vec3 m_position;
  ngl::Vec3 m_velocity;
  ngl::Vec3 m_forceAccumulator;
};


// Type definition of a vector of Particles
typedef std::vector< Particle > ParticleVector;

#endif // PARTICLE_H
