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

A truss consists of {@{typically (but not necessarily) straight members connected at joints or nodes}@}. Trusses are typically (but not necessarily) composed of {@{triangles (triangular units) because of its stability}@}. <!--SR:!2026-09-23,652,330!2026-06-25,582,330-->

The joints are likely {@{pinned support}@}, so they can {@{resist translation but not rotation}@}. <!--SR:!2028-09-02,1218,350!2028-09-11,1224,350-->

## analysis

To {@{simplify analysis}@}, {@{2}@} assumptions are often made: {@{external forces and reaction are considered to act at joints only and the weights of truss members are negligible compared to the applied loads}@}. <!--SR:!2026-11-13,692,330!2028-01-03,1029,350!2026-04-08,507,310-->

Under these assumptions, each truss member {@{must have only 2 forces acting upon it at the end joints, which must be equal in magnitude and opposite in direction (but they are not [action—reaction pair](reaction%20(physics).md))}@}. By this, each truss member is {@{either a [zero force member](zero%20force%20member.md) (0), in tension (positive values), or in compression (negative values)}@}. <!--SR:!2027-03-09,733,330!2026-08-09,617,330-->

To analyze a truss, {@{design the truss and determine the support sizes}@}. Then calculate {@{the support reactions and member forces under a specific loading condition}@} to {@{confirm that the supports and members are strong enough}@}. In detail, solve for {@{the support reactions by considering the entire truss as a free body}@}. Next, {@{solve for [forces in all members](#forces%20in%20members)}@}. <!--SR:!2027-02-18,755,330!2028-03-12,1083,350!2028-04-16,1110,350!2027-03-30,795,330!2025-06-13,301,330-->

### forces in members

There are {@{2}@} common methods to determine forces in members: {@{[method of joints](#method%20of%20joints), suitable for determining forces in all members; and method of sections, suitable for determining forces in some particular members}@}. <!--SR:!2028-07-29,1193,350!2026-08-28,584,310-->

Note that some members can have {@{zero forces, i.e. neither in tension nor in compression, which are called [zero force members](zero%20force%20member.md)}@}. <!--SR:!2028-08-12,1201,350-->

#### method of joints

The principle is simple: {@{Consider the equilibrium of each joint one by one, starting with those with 2 or less unknown forces}@}. For each joint, {@{draw the [free body diagram](free%20body%20diagram.md), and determine the axial forces of members connected to the joint}@}. <!--SR:!2026-10-06,611,310!2028-04-29,1118,350-->

Note that when a truss member is in tension, it is actually {@{pulling on the two joints instead of pushing them}@}, and vice versa for compression. <!--SR:!2025-06-16,304,330-->

The steps are {@{label all joints, members, and the support reactions}@}. Then, {@{compute the support reactions by considering the entire truss}@}. Finally, use {@{the method of joints to determine forces in all members}@}. <!--SR:!2027-05-05,820,330!2028-05-12,1130,350!2026-04-20,488,310-->

Note that after finishing with the method of joints, there is {@{no need to consider the global (the entire truss) equilibrium again}@}. This is because {@{the global equilibrium is automatically satisfied afterwards}@}, given that {@{the calculations are done correctly}@}. So this can also serve as a way to {@{check the by-hand calculations}@}. <!--SR:!2028-06-25,1165,350!2027-12-05,1005,350!2027-05-01,824,330!2026-01-12,445,310-->

## references

This text incorporates [content](https://en.wikipedia.org/wiki/truss) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
