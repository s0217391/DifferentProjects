#include <iostream>

#include "particle.h"
#include "sandPile.h"

int main(int argc, char **argv)
{


  Particle p(0.01, 2.0, ngl::Vec3(0, 10, 0));
  Sand test;

  std::cout<<"WUT" <<p.getInvMass()<<std::endl;

}
