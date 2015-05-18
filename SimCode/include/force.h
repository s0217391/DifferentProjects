#ifndef FORCE_H
#define FORCE_H

#include <vector>

#include "boost/shared_ptr.hpp"
#include "ngl/VAOPrimitives.h"

#include "particle.h"

class Force
{
public:
  virtual void exertForces(ParticleVector & io_particles) = 0;
};

//Pointers because abstract class
typedef boost::shared_ptr< Force > ForcePtr;
typedef std::vector< ForcePtr > ForcePtrVec;

#endif // FORCE_H
