# Fabric: Transfer API


## Goals
- To facilitate the transfer of transferable between participants.
### Non-goals
- To impose constraints on the logic of transfers.
- To impose constraints on how participants store and represent their states.


## Definitions
- **Transfer**
  the relocation of transferable between multiple participants
- **Transferable**
  an arbitrary amount of instances of an arbitrary type with arbitrary data that can be transferred
- **Participant**
  an arbitrary entity that can be involved in transfers
- **Controller**
  an arbitrary entity which executes the logic of transfers
### Rationale
An API should only constrain things that are part of its goal.
Anything out of scope of the goal should not be constrained.

This ensures that independent systems can work together well without giving special treatments to other systems.
Implementations can have a greater freedom when implementing the API.
Maintability is high as there are less constraints, which could be violated through reasons such as the complex interactions between different systems, made by the API.

To achieve this, only essential things are specified.
- **Transfer** is a part of the goal of this API and thus defined.
- **Transferable** represents the information being transferred in transfers.
- **Participant** represents the starting point(s) and ending point(s) of transfers.
- **Controller** represents the consumer of this API.


## Design
The API is designed with the following rules in mind:
- Expose as much information as the consumer actually needed. This reduces the implementation burden and avoids accidental violation of constraints due to the consumer.
- Clear separation of concerns. Each interface should only handle one concern.  This allows selective implementation of capabilities.
- The API should be generalized.  The zero-one-infinity rule can explain this.  Applied to this API, it means this API should not exist, should be extremely specialized for one and only one thing, or should be generalized for infinitely many cases (in the architectural aspect, we still need to respect constraints imposed by other aspects).  The fist case is...  inappropriate for obvious reasons.  Indeed, there may indeed be cases where all three of these does not make sense, such as booleans, but considering that transfer can be applied to a lot of things, the last case makes the most sense for this API.
- The API should be abstract.  The API is unlikely to be able to accomdate everything - there are almost always special cases that does not work well with the API.  However, this does not mean we should try to accomdate as much as we can.  Abstraction can help with this by remove unneeded dependencies on any particular one or one set of implementation, but instead only rely on the necessary aspects of implementations.  There may still be special cases and unremovable-but-unnecessary dependencies, but with some careful designing, most or even all of them can be avoided.
