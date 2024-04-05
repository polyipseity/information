#ifndef SPECIFICANIMAL_H
#define SPECIFICANIMAL_H

#include "Animal.h"

// ======== Carnivore class ========
class Lion : public Carnivore {
// Todo 3.1: Implement the Lion class
public:
  using Carnivore::Carnivore;
  void describe() const override;
};

class Tiger : public Carnivore {
// Todo 3.1: Implement the Tiger class
public:
  using Carnivore::Carnivore;
  void describe() const override;
};


// ======== Herbivore class ========
class Elephant : public Herbivore {
// Todo 3.2: Implement the Elephant class
public:
  using Herbivore::Herbivore;
  void describe() const override;
};

#endif // SPECIFICANIMAL_H
