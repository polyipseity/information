---
aliases:
  - truss
  - trusses
tags:
  - flashcard/active/general/eng/truss
  - language/in/English
---

# truss

## characteristics

A truss consists of {@{typically (but not necessarily) straight members connected at joints or nodes}@}. Trusses are typically (but not necessarily) composed of {@{triangles (triangular units) because of its stability}@}.

The joints are likely {@{pinned support}@}, so they can {@{resist translation but not rotation}@}.

## analysis

To {@{simplify analysis}@}, {@{2}@} assumptions are often made: {@{external forces and reaction are considered to act at joints only and the weights of truss members are negligible compared to the applied loads}@}.

Under these assumptions, each truss member {@{must have only 2 forces acting upon it at the end joints, which must be equal in magnitude and opposite in direction (but they are not [action—reaction pair](reaction%20(physics).md))}@}. By this, each truss member is {@{either a [zero force member](zero%20force%20member.md) (0), in tension (positive values), or in compression (negative values)}@}.

To analyze a truss, {@{design the truss and determine the support sizes}@}. Then calculate {@{the support reactions and member forces under a specific loading condition}@} to {@{confirm that the supports and members are strong enough}@}. In detail, solve for {@{the support reactions by considering the entire truss as a free body}@}. Next, {@{solve for [forces in all members](#forces%20in%20members)}@}.

### forces in members

There are {@{2}@} common methods to determine forces in members: {@{[method of joints](#method%20of%20joints), suitable for determining forces in all members; and method of sections, suitable for determining forces in some particular members}@}.

Note that some members can have {@{zero forces, i.e. neither in tension nor in compression, which are called [zero force members](zero%20force%20member.md)}@}.

#### method of joints

The principle is simple: {@{Consider the equilibrium of each joint one by one, starting with those with 2 or less unknown forces}@}. For each joint, {@{draw the [free body diagram](free%20body%20diagram.md), and determine the axial forces of members connected to the joint}@}.

Note that when a truss member is in tension, it is actually {@{pulling on the two joints instead of pushing them}@}, and vice versa for compression.

The steps are {@{label all joints, members, and the support reactions}@}. Then, {@{compute the support reactions by considering the entire truss}@}. Finally, use {@{the method of joints to determine forces in all members}@}.

Note that after finishing with the method of joints, there is {@{no need to consider the global (the entire truss) equilibrium again}@}. This is because {@{the global equilibrium is automatically satisfied afterwards}@}, given that {@{the calculations are done correctly}@}. So this can also serve as a way to {@{check the by-hand calculations}@}.

## references

This text incorporates [content](https://en.wikipedia.org/wiki/truss) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
